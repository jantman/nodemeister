--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT user_id_refs_id_4dc23c39;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT user_id_refs_id_40c41112;
ALTER TABLE ONLY public.enc_group_parents DROP CONSTRAINT to_group_id_refs_id_60dd650f5d1aaecf;
ALTER TABLE ONLY public.fullhistory_fullhistory DROP CONSTRAINT site_id_refs_id_7c62d298d3628153;
ALTER TABLE ONLY public.fullhistory_fullhistory DROP CONSTRAINT request_id_refs_id_1552dc7357c98b37;
ALTER TABLE ONLY public.enc_classexclusion DROP CONSTRAINT node_id_refs_id_70dab3a8987510ef;
ALTER TABLE ONLY public.enc_nodeparameter DROP CONSTRAINT node_id_refs_id_6e5d9b53f36b1b81;
ALTER TABLE ONLY public.enc_nodeclass DROP CONSTRAINT node_id_refs_id_5d776cd10aa96abe;
ALTER TABLE ONLY public.enc_paramexclusion DROP CONSTRAINT node_id_refs_id_4fff51a119028ee2;
ALTER TABLE ONLY public.enc_node_excluded_groups DROP CONSTRAINT node_id_refs_id_4cbfd3f20e178e21;
ALTER TABLE ONLY public.enc_node_groups DROP CONSTRAINT node_id_refs_id_4a6070ec50f0852b;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT group_id_refs_id_f4b32aac;
ALTER TABLE ONLY public.enc_node_excluded_groups DROP CONSTRAINT group_id_refs_id_704b1e56d7102301;
ALTER TABLE ONLY public.enc_node_groups DROP CONSTRAINT group_id_refs_id_69a7423cd6968fb3;
ALTER TABLE ONLY public.enc_groupclass DROP CONSTRAINT group_id_refs_id_2fcbc93d4fa4e6b2;
ALTER TABLE ONLY public.enc_groupparameter DROP CONSTRAINT group_id_refs_id_28df8ebc8ba1afa9;
ALTER TABLE ONLY public.enc_group_parents DROP CONSTRAINT from_group_id_refs_id_60dd650f5d1aaecf;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_fkey;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_fkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT content_type_id_refs_id_d043b34a;
ALTER TABLE ONLY public.fullhistory_fullhistory DROP CONSTRAINT content_type_id_refs_id_4f10b072e4c6121a;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_permission_id_fkey;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_fkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_permission_id_fkey;
DROP INDEX public.fullhistory_request_user_pk;
DROP INDEX public.fullhistory_fullhistory_site_id;
DROP INDEX public.fullhistory_fullhistory_request_id;
DROP INDEX public.fullhistory_fullhistory_content_type_id;
DROP INDEX public.enc_paramexclusion_node_id;
DROP INDEX public.enc_nodeparameter_node_id;
DROP INDEX public.enc_nodeclass_node_id;
DROP INDEX public.enc_node_groups_node_id;
DROP INDEX public.enc_node_groups_group_id;
DROP INDEX public.enc_node_excluded_groups_node_id;
DROP INDEX public.enc_node_excluded_groups_group_id;
DROP INDEX public.enc_groupparameter_group_id;
DROP INDEX public.enc_groupclass_group_id;
DROP INDEX public.enc_group_parents_to_group_id;
DROP INDEX public.enc_group_parents_from_group_id;
DROP INDEX public.enc_classexclusion_node_id;
DROP INDEX public.django_session_session_key_like;
DROP INDEX public.django_session_expire_date;
DROP INDEX public.django_admin_log_user_id;
DROP INDEX public.django_admin_log_content_type_id;
DROP INDEX public.auth_user_username_like;
DROP INDEX public.auth_user_user_permissions_user_id;
DROP INDEX public.auth_user_user_permissions_permission_id;
DROP INDEX public.auth_user_groups_user_id;
DROP INDEX public.auth_user_groups_group_id;
DROP INDEX public.auth_permission_content_type_id;
DROP INDEX public.auth_group_permissions_permission_id;
DROP INDEX public.auth_group_permissions_group_id;
DROP INDEX public.auth_group_name_like;
ALTER TABLE ONLY public.south_migrationhistory DROP CONSTRAINT south_migrationhistory_pkey;
ALTER TABLE ONLY public.fullhistory_request DROP CONSTRAINT fullhistory_request_pkey;
ALTER TABLE ONLY public.fullhistory_fullhistory DROP CONSTRAINT fullhistory_fullhistory_revision_434ebf90c28f01e9_uniq;
ALTER TABLE ONLY public.fullhistory_fullhistory DROP CONSTRAINT fullhistory_fullhistory_pkey;
ALTER TABLE ONLY public.enc_paramexclusion DROP CONSTRAINT enc_paramexclusion_pkey;
ALTER TABLE ONLY public.enc_paramexclusion DROP CONSTRAINT enc_paramexclusion_node_id_1f0a28cb93fd6108_uniq;
ALTER TABLE ONLY public.enc_nodeparameter DROP CONSTRAINT enc_nodeparameter_pkey;
ALTER TABLE ONLY public.enc_nodeparameter DROP CONSTRAINT enc_nodeparameter_node_id_2f2ddd93be96482e_uniq;
ALTER TABLE ONLY public.enc_nodeclass DROP CONSTRAINT enc_nodeclass_pkey;
ALTER TABLE ONLY public.enc_nodeclass DROP CONSTRAINT enc_nodeclass_node_id_d361154995afcd_uniq;
ALTER TABLE ONLY public.enc_node DROP CONSTRAINT enc_node_pkey;
ALTER TABLE ONLY public.enc_node DROP CONSTRAINT enc_node_hostname_uniq;
ALTER TABLE ONLY public.enc_node_groups DROP CONSTRAINT enc_node_groups_pkey;
ALTER TABLE ONLY public.enc_node_groups DROP CONSTRAINT enc_node_groups_node_id_79d082a253e241b9_uniq;
ALTER TABLE ONLY public.enc_node_excluded_groups DROP CONSTRAINT enc_node_excluded_groups_pkey;
ALTER TABLE ONLY public.enc_node_excluded_groups DROP CONSTRAINT enc_node_excluded_groups_node_id_6721cef43cb14085_uniq;
ALTER TABLE ONLY public.enc_groupparameter DROP CONSTRAINT enc_groupparameter_pkey;
ALTER TABLE ONLY public.enc_groupparameter DROP CONSTRAINT enc_groupparameter_paramkey_2c9c831d8bdd38da_uniq;
ALTER TABLE ONLY public.enc_groupclass DROP CONSTRAINT enc_groupclass_pkey;
ALTER TABLE ONLY public.enc_groupclass DROP CONSTRAINT enc_groupclass_classname_483d91ac8bfab5b5_uniq;
ALTER TABLE ONLY public.enc_group DROP CONSTRAINT enc_group_pkey;
ALTER TABLE ONLY public.enc_group_parents DROP CONSTRAINT enc_group_parents_pkey;
ALTER TABLE ONLY public.enc_group_parents DROP CONSTRAINT enc_group_parents_from_group_id_5e63858679675148_uniq;
ALTER TABLE ONLY public.enc_group DROP CONSTRAINT enc_group_name_uniq;
ALTER TABLE ONLY public.enc_classexclusion DROP CONSTRAINT enc_classexclusion_pkey;
ALTER TABLE ONLY public.enc_classexclusion DROP CONSTRAINT enc_classexclusion_node_id_7bee38a96bb9aa19_uniq;
ALTER TABLE ONLY public.django_site DROP CONSTRAINT django_site_pkey;
ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_key;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_key;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_key;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_key;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_key;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
ALTER TABLE public.south_migrationhistory ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.fullhistory_request ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.fullhistory_fullhistory ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.enc_paramexclusion ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.enc_nodeparameter ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.enc_nodeclass ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.enc_node_groups ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.enc_node_excluded_groups ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.enc_node ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.enc_groupparameter ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.enc_groupclass ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.enc_group_parents ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.enc_group ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.enc_classexclusion ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_site ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE public.south_migrationhistory_id_seq;
DROP TABLE public.south_migrationhistory;
DROP SEQUENCE public.fullhistory_request_id_seq;
DROP TABLE public.fullhistory_request;
DROP SEQUENCE public.fullhistory_fullhistory_id_seq;
DROP TABLE public.fullhistory_fullhistory;
DROP SEQUENCE public.enc_paramexclusion_id_seq;
DROP TABLE public.enc_paramexclusion;
DROP SEQUENCE public.enc_nodeparameter_id_seq;
DROP TABLE public.enc_nodeparameter;
DROP SEQUENCE public.enc_nodeclass_id_seq;
DROP TABLE public.enc_nodeclass;
DROP SEQUENCE public.enc_node_id_seq;
DROP SEQUENCE public.enc_node_groups_id_seq;
DROP TABLE public.enc_node_groups;
DROP SEQUENCE public.enc_node_excluded_groups_id_seq;
DROP TABLE public.enc_node_excluded_groups;
DROP TABLE public.enc_node;
DROP SEQUENCE public.enc_groupparameter_id_seq;
DROP TABLE public.enc_groupparameter;
DROP SEQUENCE public.enc_groupclass_id_seq;
DROP TABLE public.enc_groupclass;
DROP SEQUENCE public.enc_group_parents_id_seq;
DROP TABLE public.enc_group_parents;
DROP SEQUENCE public.enc_group_id_seq;
DROP TABLE public.enc_group;
DROP SEQUENCE public.enc_classexclusion_id_seq;
DROP TABLE public.enc_classexclusion;
DROP SEQUENCE public.django_site_id_seq;
DROP TABLE public.django_site;
DROP TABLE public.django_session;
DROP SEQUENCE public.django_content_type_id_seq;
DROP TABLE public.django_content_type;
DROP SEQUENCE public.django_admin_log_id_seq;
DROP TABLE public.django_admin_log;
DROP SEQUENCE public.auth_user_user_permissions_id_seq;
DROP TABLE public.auth_user_user_permissions;
DROP SEQUENCE public.auth_user_id_seq;
DROP SEQUENCE public.auth_user_groups_id_seq;
DROP TABLE public.auth_user_groups;
DROP TABLE public.auth_user;
DROP SEQUENCE public.auth_permission_id_seq;
DROP TABLE public.auth_permission;
DROP SEQUENCE public.auth_group_permissions_id_seq;
DROP TABLE public.auth_group_permissions;
DROP SEQUENCE public.auth_group_id_seq;
DROP TABLE public.auth_group;
DROP EXTENSION plpgsql;
DROP SCHEMA public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO nodemeister;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO nodemeister;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO nodemeister;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO nodemeister;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO nodemeister;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO nodemeister;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO nodemeister;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO nodemeister;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO nodemeister;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO nodemeister;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO nodemeister;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO nodemeister;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO nodemeister;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO nodemeister;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO nodemeister;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO nodemeister;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO nodemeister;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO nodemeister;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO nodemeister;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: enc_classexclusion; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE enc_classexclusion (
    id integer NOT NULL,
    node_id integer NOT NULL,
    exclusion character varying(200) NOT NULL
);


ALTER TABLE public.enc_classexclusion OWNER TO nodemeister;

--
-- Name: enc_classexclusion_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE enc_classexclusion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enc_classexclusion_id_seq OWNER TO nodemeister;

--
-- Name: enc_classexclusion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE enc_classexclusion_id_seq OWNED BY enc_classexclusion.id;


--
-- Name: enc_group; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE enc_group (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    description character varying(200) NOT NULL
);


ALTER TABLE public.enc_group OWNER TO nodemeister;

--
-- Name: enc_group_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE enc_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enc_group_id_seq OWNER TO nodemeister;

--
-- Name: enc_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE enc_group_id_seq OWNED BY enc_group.id;


--
-- Name: enc_group_parents; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE enc_group_parents (
    id integer NOT NULL,
    from_group_id integer NOT NULL,
    to_group_id integer NOT NULL
);


ALTER TABLE public.enc_group_parents OWNER TO nodemeister;

--
-- Name: enc_group_parents_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE enc_group_parents_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enc_group_parents_id_seq OWNER TO nodemeister;

--
-- Name: enc_group_parents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE enc_group_parents_id_seq OWNED BY enc_group_parents.id;


--
-- Name: enc_groupclass; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE enc_groupclass (
    id integer NOT NULL,
    group_id integer NOT NULL,
    classname character varying(200) NOT NULL,
    classparams json NOT NULL
);


ALTER TABLE public.enc_groupclass OWNER TO nodemeister;

--
-- Name: enc_groupclass_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE enc_groupclass_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enc_groupclass_id_seq OWNER TO nodemeister;

--
-- Name: enc_groupclass_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE enc_groupclass_id_seq OWNED BY enc_groupclass.id;


--
-- Name: enc_groupparameter; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE enc_groupparameter (
    id integer NOT NULL,
    group_id integer NOT NULL,
    paramkey character varying(200) NOT NULL,
    paramvalue json NOT NULL
);


ALTER TABLE public.enc_groupparameter OWNER TO nodemeister;

--
-- Name: enc_groupparameter_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE enc_groupparameter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enc_groupparameter_id_seq OWNER TO nodemeister;

--
-- Name: enc_groupparameter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE enc_groupparameter_id_seq OWNED BY enc_groupparameter.id;


--
-- Name: enc_node; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE enc_node (
    id integer NOT NULL,
    hostname character varying(200) NOT NULL,
    description character varying(200) NOT NULL
);


ALTER TABLE public.enc_node OWNER TO nodemeister;

--
-- Name: enc_node_excluded_groups; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE enc_node_excluded_groups (
    id integer NOT NULL,
    node_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.enc_node_excluded_groups OWNER TO nodemeister;

--
-- Name: enc_node_excluded_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE enc_node_excluded_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enc_node_excluded_groups_id_seq OWNER TO nodemeister;

--
-- Name: enc_node_excluded_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE enc_node_excluded_groups_id_seq OWNED BY enc_node_excluded_groups.id;


--
-- Name: enc_node_groups; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE enc_node_groups (
    id integer NOT NULL,
    node_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.enc_node_groups OWNER TO nodemeister;

--
-- Name: enc_node_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE enc_node_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enc_node_groups_id_seq OWNER TO nodemeister;

--
-- Name: enc_node_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE enc_node_groups_id_seq OWNED BY enc_node_groups.id;


--
-- Name: enc_node_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE enc_node_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enc_node_id_seq OWNER TO nodemeister;

--
-- Name: enc_node_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE enc_node_id_seq OWNED BY enc_node.id;


--
-- Name: enc_nodeclass; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE enc_nodeclass (
    id integer NOT NULL,
    node_id integer NOT NULL,
    classname character varying(200) NOT NULL,
    classparams json NOT NULL
);


ALTER TABLE public.enc_nodeclass OWNER TO nodemeister;

--
-- Name: enc_nodeclass_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE enc_nodeclass_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enc_nodeclass_id_seq OWNER TO nodemeister;

--
-- Name: enc_nodeclass_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE enc_nodeclass_id_seq OWNED BY enc_nodeclass.id;


--
-- Name: enc_nodeparameter; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE enc_nodeparameter (
    id integer NOT NULL,
    node_id integer NOT NULL,
    paramkey character varying(200) NOT NULL,
    paramvalue json NOT NULL
);


ALTER TABLE public.enc_nodeparameter OWNER TO nodemeister;

--
-- Name: enc_nodeparameter_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE enc_nodeparameter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enc_nodeparameter_id_seq OWNER TO nodemeister;

--
-- Name: enc_nodeparameter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE enc_nodeparameter_id_seq OWNED BY enc_nodeparameter.id;


--
-- Name: enc_paramexclusion; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE enc_paramexclusion (
    id integer NOT NULL,
    node_id integer NOT NULL,
    exclusion character varying(200) NOT NULL
);


ALTER TABLE public.enc_paramexclusion OWNER TO nodemeister;

--
-- Name: enc_paramexclusion_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE enc_paramexclusion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.enc_paramexclusion_id_seq OWNER TO nodemeister;

--
-- Name: enc_paramexclusion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE enc_paramexclusion_id_seq OWNED BY enc_paramexclusion.id;


--
-- Name: fullhistory_fullhistory; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE fullhistory_fullhistory (
    id integer NOT NULL,
    content_type_id integer NOT NULL,
    object_id character varying(255) NOT NULL,
    revision integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    data text NOT NULL,
    request_id integer,
    site_id integer NOT NULL,
    action character varying(1) NOT NULL,
    info text NOT NULL,
    CONSTRAINT fullhistory_fullhistory_revision_check CHECK ((revision >= 0))
);


ALTER TABLE public.fullhistory_fullhistory OWNER TO nodemeister;

--
-- Name: fullhistory_fullhistory_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE fullhistory_fullhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fullhistory_fullhistory_id_seq OWNER TO nodemeister;

--
-- Name: fullhistory_fullhistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE fullhistory_fullhistory_id_seq OWNED BY fullhistory_fullhistory.id;


--
-- Name: fullhistory_request; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE fullhistory_request (
    id integer NOT NULL,
    user_name character varying(255),
    user_pk integer,
    request_path character varying(255),
    CONSTRAINT fullhistory_request_user_pk_check CHECK ((user_pk >= 0))
);


ALTER TABLE public.fullhistory_request OWNER TO nodemeister;

--
-- Name: fullhistory_request_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE fullhistory_request_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fullhistory_request_id_seq OWNER TO nodemeister;

--
-- Name: fullhistory_request_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE fullhistory_request_id_seq OWNED BY fullhistory_request.id;


--
-- Name: south_migrationhistory; Type: TABLE; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE TABLE south_migrationhistory (
    id integer NOT NULL,
    app_name character varying(255) NOT NULL,
    migration character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.south_migrationhistory OWNER TO nodemeister;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE; Schema: public; Owner: nodemeister
--

CREATE SEQUENCE south_migrationhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.south_migrationhistory_id_seq OWNER TO nodemeister;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nodemeister
--

ALTER SEQUENCE south_migrationhistory_id_seq OWNED BY south_migrationhistory.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_classexclusion ALTER COLUMN id SET DEFAULT nextval('enc_classexclusion_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_group ALTER COLUMN id SET DEFAULT nextval('enc_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_group_parents ALTER COLUMN id SET DEFAULT nextval('enc_group_parents_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_groupclass ALTER COLUMN id SET DEFAULT nextval('enc_groupclass_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_groupparameter ALTER COLUMN id SET DEFAULT nextval('enc_groupparameter_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_node ALTER COLUMN id SET DEFAULT nextval('enc_node_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_node_excluded_groups ALTER COLUMN id SET DEFAULT nextval('enc_node_excluded_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_node_groups ALTER COLUMN id SET DEFAULT nextval('enc_node_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_nodeclass ALTER COLUMN id SET DEFAULT nextval('enc_nodeclass_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_nodeparameter ALTER COLUMN id SET DEFAULT nextval('enc_nodeparameter_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_paramexclusion ALTER COLUMN id SET DEFAULT nextval('enc_paramexclusion_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY fullhistory_fullhistory ALTER COLUMN id SET DEFAULT nextval('fullhistory_fullhistory_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY fullhistory_request ALTER COLUMN id SET DEFAULT nextval('fullhistory_request_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY south_migrationhistory ALTER COLUMN id SET DEFAULT nextval('south_migrationhistory_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add content type	4	add_contenttype
11	Can change content type	4	change_contenttype
12	Can delete content type	4	delete_contenttype
13	Can add session	5	add_session
14	Can change session	5	change_session
15	Can delete session	5	delete_session
16	Can add site	6	add_site
17	Can change site	6	change_site
18	Can delete site	6	delete_site
19	Can add log entry	7	add_logentry
20	Can change log entry	7	change_logentry
21	Can delete log entry	7	delete_logentry
22	Can add migration history	8	add_migrationhistory
23	Can change migration history	8	change_migrationhistory
24	Can delete migration history	8	delete_migrationhistory
25	Can add group	9	add_group
26	Can change group	9	change_group
27	Can delete group	9	delete_group
28	Can add node	10	add_node
29	Can change node	10	change_node
30	Can delete node	10	delete_node
31	Can add group class	11	add_groupclass
32	Can change group class	11	change_groupclass
33	Can delete group class	11	delete_groupclass
34	Can add node class	12	add_nodeclass
35	Can change node class	12	change_nodeclass
36	Can delete node class	12	delete_nodeclass
37	Can add group parameter	13	add_groupparameter
38	Can change group parameter	13	change_groupparameter
39	Can delete group parameter	13	delete_groupparameter
40	Can add node parameter	14	add_nodeparameter
41	Can change node parameter	14	change_nodeparameter
42	Can delete node parameter	14	delete_nodeparameter
43	Can add param exclusion	15	add_paramexclusion
44	Can change param exclusion	15	change_paramexclusion
45	Can delete param exclusion	15	delete_paramexclusion
46	Can add class exclusion	16	add_classexclusion
47	Can change class exclusion	16	change_classexclusion
48	Can delete class exclusion	16	delete_classexclusion
49	Can add request	17	add_request
50	Can change request	17	change_request
51	Can delete request	17	delete_request
52	Can add full history	18	add_fullhistory
53	Can change full history	18	change_fullhistory
54	Can delete full history	18	delete_fullhistory
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('auth_permission_id_seq', 54, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$10000$xDmVXlPMRQsp$kCcoRNiEs1ifvVmEd1cENle4UMWRee9GvupDHX+KlRg=	2013-11-25 19:33:42.21438-05	t	admin			admin@example.com	t	t	2013-11-24 22:10:14.806124-05
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	content type	contenttypes	contenttype
5	session	sessions	session
6	site	sites	site
7	log entry	admin	logentry
8	migration history	south	migrationhistory
9	group	enc	group
10	node	enc	node
11	group class	enc	groupclass
12	node class	enc	nodeclass
13	group parameter	enc	groupparameter
14	node parameter	enc	nodeparameter
15	param exclusion	enc	paramexclusion
16	class exclusion	enc	classexclusion
17	request	fullhistory	request
18	full history	fullhistory	fullhistory
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('django_content_type_id_seq', 18, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
n70ceob9t0f82rq8vhqtql1hroytd8ei	ZTBlZWIyNTE5ZDJkYjY0NzU3M2I2ZTRlMDMwZDg2MWNmMTBkYTgxNDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu	2013-12-09 14:18:34.955591-05
55fi0wecng3d7zr72ivo2r1pdlj871iu	ZTBlZWIyNTE5ZDJkYjY0NzU3M2I2ZTRlMDMwZDg2MWNmMTBkYTgxNDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu	2013-12-09 19:33:42.220002-05
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Data for Name: enc_classexclusion; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY enc_classexclusion (id, node_id, exclusion) FROM stdin;
1	1	class_group1_bar
\.


--
-- Name: enc_classexclusion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('enc_classexclusion_id_seq', 1, true);


--
-- Data for Name: enc_group; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY enc_group (id, name, description) FROM stdin;
1	group1	groupOne
\.


--
-- Name: enc_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('enc_group_id_seq', 1, true);


--
-- Data for Name: enc_group_parents; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY enc_group_parents (id, from_group_id, to_group_id) FROM stdin;
\.


--
-- Name: enc_group_parents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('enc_group_parents_id_seq', 1, false);


--
-- Data for Name: enc_groupclass; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY enc_groupclass (id, group_id, classname, classparams) FROM stdin;
1	1	class_group1_foo	{"foo_grp1":"bar_grp1"}
2	1	class_group1_bar	{"bar_grp1":"baz"}
\.


--
-- Name: enc_groupclass_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('enc_groupclass_id_seq', 2, true);


--
-- Data for Name: enc_groupparameter; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY enc_groupparameter (id, group_id, paramkey, paramvalue) FROM stdin;
2	1	param_group1_bar	{"fooG1param":"bar"}
3	1	param_group1_baz	{"foo":"param_group1_baz"}
\.


--
-- Name: enc_groupparameter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('enc_groupparameter_id_seq', 3, true);


--
-- Data for Name: enc_node; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY enc_node (id, hostname, description) FROM stdin;
1	testnode	testnode_description
\.


--
-- Data for Name: enc_node_excluded_groups; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY enc_node_excluded_groups (id, node_id, group_id) FROM stdin;
\.


--
-- Name: enc_node_excluded_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('enc_node_excluded_groups_id_seq', 1, false);


--
-- Data for Name: enc_node_groups; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY enc_node_groups (id, node_id, group_id) FROM stdin;
3	1	1
\.


--
-- Name: enc_node_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('enc_node_groups_id_seq', 3, true);


--
-- Name: enc_node_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('enc_node_id_seq', 1, true);


--
-- Data for Name: enc_nodeclass; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY enc_nodeclass (id, node_id, classname, classparams) FROM stdin;
1	1	barclass	null
\.


--
-- Name: enc_nodeclass_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('enc_nodeclass_id_seq', 1, true);


--
-- Data for Name: enc_nodeparameter; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY enc_nodeparameter (id, node_id, paramkey, paramvalue) FROM stdin;
2	1	foo_param	{"foo":"bar"}
\.


--
-- Name: enc_nodeparameter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('enc_nodeparameter_id_seq', 2, true);


--
-- Data for Name: enc_paramexclusion; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY enc_paramexclusion (id, node_id, exclusion) FROM stdin;
\.


--
-- Name: enc_paramexclusion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('enc_paramexclusion_id_seq', 1, false);


--
-- Data for Name: fullhistory_fullhistory; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY fullhistory_fullhistory (id, content_type_id, object_id, revision, action_time, data, request_id, site_id, action, info) FROM stdin;
1	10	1	0	2013-11-25 14:18:19.594317-05	{"excluded_groups": [[]], "hostname": ["testnode"], "description": ["testnode_description"], "groups": [[]], "id": [1]}	1	1	C	(System) Created
2	10	1	1	2013-11-25 14:18:53.732009-05	{}	2	1	U	admin Updated
3	14	1	0	2013-11-25 14:18:53.739145-05	{"node": [1], "paramkey": ["param_one"], "paramvalue": ["\\"param one\\""], "id": [1]}	2	1	C	admin Created
4	10	1	2	2013-11-25 19:41:47.118364-05	{}	3	1	U	admin Updated
5	14	2	0	2013-11-25 19:41:47.133255-05	{"node": [1], "paramkey": ["foo_param"], "paramvalue": ["{\\"foo\\":\\"bar\\"}"], "id": [2]}	3	1	C	admin Created
6	10	1	3	2013-11-25 19:41:58.860245-05	{}	4	1	U	admin Updated
7	12	1	0	2013-11-25 19:41:58.872787-05	{"node": [1], "classname": ["barclass"], "id": [1], "classparams": [null]}	4	1	C	admin Created
8	14	2	1	2013-11-25 19:41:58.884213-05	{}	4	1	U	admin Updated
9	9	1	0	2013-11-25 19:42:49.565264-05	{"id": [1], "parents": [[]], "name": ["group1"], "description": ["groupOne"]}	5	1	C	admin Created
10	9	1	1	2013-11-25 19:43:05.234234-05	{}	6	1	U	admin Updated
11	9	1	2	2013-11-25 19:44:55.026056-05	{}	7	1	U	admin Updated
13	14	2	2	2013-11-25 19:45:32.816177-05	{}	8	1	U	admin Updated
12	10	1	4	2013-11-25 19:45:32.795454-05	{"groups": ["", "group1 (id=1)"]}	8	1	U	admin Updated
14	9	1	3	2013-11-25 19:46:45.380572-05	{}	9	1	U	admin Updated
15	10	1	5	2013-11-25 19:47:27.784813-05	{}	10	1	U	admin Updated
16	14	2	3	2013-11-25 19:47:27.80909-05	{}	10	1	U	admin Updated
\.


--
-- Name: fullhistory_fullhistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('fullhistory_fullhistory_id_seq', 16, true);


--
-- Data for Name: fullhistory_request; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY fullhistory_request (id, user_name, user_pk, request_path) FROM stdin;
1	(System)	\N	\N
2	admin	1	/admin/enc/node/1/
3	admin	1	/admin/enc/node/1/
4	admin	1	/admin/enc/node/1/
5	admin	1	/admin/enc/group/add/
6	admin	1	/admin/enc/group/1/
7	admin	1	/admin/enc/group/1/
8	admin	1	/admin/enc/node/1/
9	admin	1	/admin/enc/group/1/
10	admin	1	/admin/enc/node/1/
\.


--
-- Name: fullhistory_request_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('fullhistory_request_id_seq', 10, true);


--
-- Data for Name: south_migrationhistory; Type: TABLE DATA; Schema: public; Owner: nodemeister
--

COPY south_migrationhistory (id, app_name, migration, applied) FROM stdin;
1	enc	0001_initial	2013-11-24 22:10:20.759807-05
2	enc	0002_auto__add_unique_nodeparameter_node_key__add_unique_paramexclusion_nod	2013-11-24 22:10:20.84012-05
3	enc	0003_auto	2013-11-24 22:10:20.902894-05
4	enc	0004_auto__del_field_nodeparameter_value__del_field_nodeparameter_key__add_	2013-11-24 22:10:21.069707-05
5	fullhistory	0001_initial	2013-11-24 22:10:21.238138-05
\.


--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nodemeister
--

SELECT pg_catalog.setval('south_migrationhistory_id_seq', 5, true);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: enc_classexclusion_node_id_7bee38a96bb9aa19_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_classexclusion
    ADD CONSTRAINT enc_classexclusion_node_id_7bee38a96bb9aa19_uniq UNIQUE (node_id, exclusion);


--
-- Name: enc_classexclusion_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_classexclusion
    ADD CONSTRAINT enc_classexclusion_pkey PRIMARY KEY (id);


--
-- Name: enc_group_name_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_group
    ADD CONSTRAINT enc_group_name_uniq UNIQUE (name);


--
-- Name: enc_group_parents_from_group_id_5e63858679675148_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_group_parents
    ADD CONSTRAINT enc_group_parents_from_group_id_5e63858679675148_uniq UNIQUE (from_group_id, to_group_id);


--
-- Name: enc_group_parents_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_group_parents
    ADD CONSTRAINT enc_group_parents_pkey PRIMARY KEY (id);


--
-- Name: enc_group_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_group
    ADD CONSTRAINT enc_group_pkey PRIMARY KEY (id);


--
-- Name: enc_groupclass_classname_483d91ac8bfab5b5_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_groupclass
    ADD CONSTRAINT enc_groupclass_classname_483d91ac8bfab5b5_uniq UNIQUE (classname, group_id);


--
-- Name: enc_groupclass_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_groupclass
    ADD CONSTRAINT enc_groupclass_pkey PRIMARY KEY (id);


--
-- Name: enc_groupparameter_paramkey_2c9c831d8bdd38da_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_groupparameter
    ADD CONSTRAINT enc_groupparameter_paramkey_2c9c831d8bdd38da_uniq UNIQUE (paramkey, group_id);


--
-- Name: enc_groupparameter_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_groupparameter
    ADD CONSTRAINT enc_groupparameter_pkey PRIMARY KEY (id);


--
-- Name: enc_node_excluded_groups_node_id_6721cef43cb14085_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_node_excluded_groups
    ADD CONSTRAINT enc_node_excluded_groups_node_id_6721cef43cb14085_uniq UNIQUE (node_id, group_id);


--
-- Name: enc_node_excluded_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_node_excluded_groups
    ADD CONSTRAINT enc_node_excluded_groups_pkey PRIMARY KEY (id);


--
-- Name: enc_node_groups_node_id_79d082a253e241b9_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_node_groups
    ADD CONSTRAINT enc_node_groups_node_id_79d082a253e241b9_uniq UNIQUE (node_id, group_id);


--
-- Name: enc_node_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_node_groups
    ADD CONSTRAINT enc_node_groups_pkey PRIMARY KEY (id);


--
-- Name: enc_node_hostname_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_node
    ADD CONSTRAINT enc_node_hostname_uniq UNIQUE (hostname);


--
-- Name: enc_node_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_node
    ADD CONSTRAINT enc_node_pkey PRIMARY KEY (id);


--
-- Name: enc_nodeclass_node_id_d361154995afcd_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_nodeclass
    ADD CONSTRAINT enc_nodeclass_node_id_d361154995afcd_uniq UNIQUE (node_id, classname);


--
-- Name: enc_nodeclass_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_nodeclass
    ADD CONSTRAINT enc_nodeclass_pkey PRIMARY KEY (id);


--
-- Name: enc_nodeparameter_node_id_2f2ddd93be96482e_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_nodeparameter
    ADD CONSTRAINT enc_nodeparameter_node_id_2f2ddd93be96482e_uniq UNIQUE (node_id, paramkey);


--
-- Name: enc_nodeparameter_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_nodeparameter
    ADD CONSTRAINT enc_nodeparameter_pkey PRIMARY KEY (id);


--
-- Name: enc_paramexclusion_node_id_1f0a28cb93fd6108_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_paramexclusion
    ADD CONSTRAINT enc_paramexclusion_node_id_1f0a28cb93fd6108_uniq UNIQUE (node_id, exclusion);


--
-- Name: enc_paramexclusion_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY enc_paramexclusion
    ADD CONSTRAINT enc_paramexclusion_pkey PRIMARY KEY (id);


--
-- Name: fullhistory_fullhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY fullhistory_fullhistory
    ADD CONSTRAINT fullhistory_fullhistory_pkey PRIMARY KEY (id);


--
-- Name: fullhistory_fullhistory_revision_434ebf90c28f01e9_uniq; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY fullhistory_fullhistory
    ADD CONSTRAINT fullhistory_fullhistory_revision_434ebf90c28f01e9_uniq UNIQUE (revision, content_type_id, object_id);


--
-- Name: fullhistory_request_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY fullhistory_request
    ADD CONSTRAINT fullhistory_request_pkey PRIMARY KEY (id);


--
-- Name: south_migrationhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: nodemeister; Tablespace: 
--

ALTER TABLE ONLY south_migrationhistory
    ADD CONSTRAINT south_migrationhistory_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_like; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX auth_group_name_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_like; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX auth_user_username_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_like; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: enc_classexclusion_node_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_classexclusion_node_id ON enc_classexclusion USING btree (node_id);


--
-- Name: enc_group_parents_from_group_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_group_parents_from_group_id ON enc_group_parents USING btree (from_group_id);


--
-- Name: enc_group_parents_to_group_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_group_parents_to_group_id ON enc_group_parents USING btree (to_group_id);


--
-- Name: enc_groupclass_group_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_groupclass_group_id ON enc_groupclass USING btree (group_id);


--
-- Name: enc_groupparameter_group_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_groupparameter_group_id ON enc_groupparameter USING btree (group_id);


--
-- Name: enc_node_excluded_groups_group_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_node_excluded_groups_group_id ON enc_node_excluded_groups USING btree (group_id);


--
-- Name: enc_node_excluded_groups_node_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_node_excluded_groups_node_id ON enc_node_excluded_groups USING btree (node_id);


--
-- Name: enc_node_groups_group_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_node_groups_group_id ON enc_node_groups USING btree (group_id);


--
-- Name: enc_node_groups_node_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_node_groups_node_id ON enc_node_groups USING btree (node_id);


--
-- Name: enc_nodeclass_node_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_nodeclass_node_id ON enc_nodeclass USING btree (node_id);


--
-- Name: enc_nodeparameter_node_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_nodeparameter_node_id ON enc_nodeparameter USING btree (node_id);


--
-- Name: enc_paramexclusion_node_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX enc_paramexclusion_node_id ON enc_paramexclusion USING btree (node_id);


--
-- Name: fullhistory_fullhistory_content_type_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX fullhistory_fullhistory_content_type_id ON fullhistory_fullhistory USING btree (content_type_id);


--
-- Name: fullhistory_fullhistory_request_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX fullhistory_fullhistory_request_id ON fullhistory_fullhistory USING btree (request_id);


--
-- Name: fullhistory_fullhistory_site_id; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX fullhistory_fullhistory_site_id ON fullhistory_fullhistory USING btree (site_id);


--
-- Name: fullhistory_request_user_pk; Type: INDEX; Schema: public; Owner: nodemeister; Tablespace: 
--

CREATE INDEX fullhistory_request_user_pk ON fullhistory_request USING btree (user_pk);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_4f10b072e4c6121a; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY fullhistory_fullhistory
    ADD CONSTRAINT content_type_id_refs_id_4f10b072e4c6121a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_d043b34a; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: from_group_id_refs_id_60dd650f5d1aaecf; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_group_parents
    ADD CONSTRAINT from_group_id_refs_id_60dd650f5d1aaecf FOREIGN KEY (from_group_id) REFERENCES enc_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_28df8ebc8ba1afa9; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_groupparameter
    ADD CONSTRAINT group_id_refs_id_28df8ebc8ba1afa9 FOREIGN KEY (group_id) REFERENCES enc_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_2fcbc93d4fa4e6b2; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_groupclass
    ADD CONSTRAINT group_id_refs_id_2fcbc93d4fa4e6b2 FOREIGN KEY (group_id) REFERENCES enc_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_69a7423cd6968fb3; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_node_groups
    ADD CONSTRAINT group_id_refs_id_69a7423cd6968fb3 FOREIGN KEY (group_id) REFERENCES enc_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_704b1e56d7102301; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_node_excluded_groups
    ADD CONSTRAINT group_id_refs_id_704b1e56d7102301 FOREIGN KEY (group_id) REFERENCES enc_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_f4b32aac; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: node_id_refs_id_4a6070ec50f0852b; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_node_groups
    ADD CONSTRAINT node_id_refs_id_4a6070ec50f0852b FOREIGN KEY (node_id) REFERENCES enc_node(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: node_id_refs_id_4cbfd3f20e178e21; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_node_excluded_groups
    ADD CONSTRAINT node_id_refs_id_4cbfd3f20e178e21 FOREIGN KEY (node_id) REFERENCES enc_node(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: node_id_refs_id_4fff51a119028ee2; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_paramexclusion
    ADD CONSTRAINT node_id_refs_id_4fff51a119028ee2 FOREIGN KEY (node_id) REFERENCES enc_node(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: node_id_refs_id_5d776cd10aa96abe; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_nodeclass
    ADD CONSTRAINT node_id_refs_id_5d776cd10aa96abe FOREIGN KEY (node_id) REFERENCES enc_node(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: node_id_refs_id_6e5d9b53f36b1b81; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_nodeparameter
    ADD CONSTRAINT node_id_refs_id_6e5d9b53f36b1b81 FOREIGN KEY (node_id) REFERENCES enc_node(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: node_id_refs_id_70dab3a8987510ef; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_classexclusion
    ADD CONSTRAINT node_id_refs_id_70dab3a8987510ef FOREIGN KEY (node_id) REFERENCES enc_node(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: request_id_refs_id_1552dc7357c98b37; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY fullhistory_fullhistory
    ADD CONSTRAINT request_id_refs_id_1552dc7357c98b37 FOREIGN KEY (request_id) REFERENCES fullhistory_request(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: site_id_refs_id_7c62d298d3628153; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY fullhistory_fullhistory
    ADD CONSTRAINT site_id_refs_id_7c62d298d3628153 FOREIGN KEY (site_id) REFERENCES django_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: to_group_id_refs_id_60dd650f5d1aaecf; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY enc_group_parents
    ADD CONSTRAINT to_group_id_refs_id_60dd650f5d1aaecf FOREIGN KEY (to_group_id) REFERENCES enc_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_40c41112; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_40c41112 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_4dc23c39; Type: FK CONSTRAINT; Schema: public; Owner: nodemeister
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_4dc23c39 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

