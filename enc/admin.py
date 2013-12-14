from django.contrib import admin
from django import forms
from models import *
from fullhistory.admin import FullHistoryAdmin


class GroupClassesInline(admin.TabularInline):
    model = GroupClass
    extra = 1
        
class GroupParamsInline(admin.TabularInline):
    model = GroupParameter
    extra = 1


class NodeClassesInline(admin.TabularInline):
    model = NodeClass
    extra = 1
    parent_fieldset = 'Properties'
        
class NodeParamsInline(admin.TabularInline):
    model = NodeParameter
    extra = 1
    parent_fieldset = 'Properties'

class ClassExclusionInline(admin.TabularInline):
    model = ClassExclusion
    extra = 1
    parent_fieldset = 'Exclusions'

class ParamExclusionInline(admin.TabularInline):
    model = ParamExclusion
    extra = 1
    parent_fieldset = 'Exclusions'
    

class GroupNodesForm(forms.ModelForm):
    class Meta:
        model = Group
    nodes = forms.ModelMultipleChoiceField(
        queryset=Node.objects.all(),
        required=False,
        widget=admin.widgets.FilteredSelectMultiple(
            verbose_name=('Nodes'),
            is_stacked=False
        )
    )
    def __init__(self, *args, **kwargs):
        super(GroupNodesForm, self).__init__(*args, **kwargs)
	if self.instance.pk:
	    self.fields['nodes'].initial = self.instance.nodes.all()

    def save(self, commit=True):
        group = super(GroupNodesForm, self).save(commit=False)  
        if commit:
            group.save()

        if group.pk:
            group.nodes = self.cleaned_data['nodes']
            self.save_m2m()
            
        return group

class GroupNodesForm(forms.ModelForm):
    class Meta:
        model = Group
    nodes = forms.ModelMultipleChoiceField(
        queryset=Node.objects.all(),
        required=False,
        widget=admin.widgets.FilteredSelectMultiple(
            verbose_name=('Nodes'),
            is_stacked=False
        )
    )

    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=admin.widgets.FilteredSelectMultiple(
            verbose_name=('Nodes'),
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(GroupNodesForm, self).__init__(*args, **kwargs)
	if self.instance.pk:
	    self.fields['nodes'].initial = self.instance.nodes.all()
	    self.fields['groups'].initial = self.instance.groups.all()

    def save(self, commit=True):
        group = super(GroupNodesForm, self).save(commit=False)  
        if commit:
            group.save()

        if group.pk:
            group.nodes = self.cleaned_data['nodes']
            group.groups = self.cleaned_data['groups']
            self.save_m2m()
            
        return group



class NodeAdmin(FullHistoryAdmin):
    inlines = [NodeClassesInline,NodeParamsInline,ClassExclusionInline,ParamExclusionInline]
    #exclude = ('groups', )
    filter_horizontal = ['groups','excluded_groups']
    fieldsets = ((None, {'fields': ('hostname','description','groups')}),('Properties',{'fields':()}),('Exclusions',{'fields':('excluded_groups',)}))
    search_fields = ['hostname','classes__classname','parameters__paramkey']

class GroupAdmin(FullHistoryAdmin):
    inlines = [GroupClassesInline,GroupParamsInline]
    #exclude = ('nodes', )
    form = GroupNodesForm
    filter_horizontal = ['parents']
    search_fields = ['name','classes__classname','parameters__paramkey']



admin.site.register(Group, GroupAdmin)


admin.site.register(Node, NodeAdmin)
