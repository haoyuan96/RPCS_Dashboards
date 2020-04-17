--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 12.2 (Ubuntu 12.2-2.pgdg18.04+1)

-- Started on 2020-04-02 15:10:19 EDT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2 (class 3079 OID 20943)
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- TOC entry 3913 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


SET default_tablespace = '';

--
-- TOC entry 197 (class 1259 OID 20980)
-- Name: accels; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.accels (
    id uuid DEFAULT public.gen_random_uuid() NOT NULL,
    accel_id uuid NOT NULL,
    description character varying(255) NOT NULL,
    patient_id uuid NOT NULL,
    x numeric,
    y numeric,
    z numeric,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone
);


ALTER TABLE public.accels OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 20988)
-- Name: biometric; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.biometric (
    id uuid DEFAULT public.gen_random_uuid() NOT NULL,
    patient_id uuid NOT NULL,
    heart_rate numeric,
    blood_pressure numeric,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone
);


ALTER TABLE public.biometric OWNER TO postgres;

--
-- TOC entry 3914 (class 0 OID 0)
-- Dependencies: 198
-- Name: COLUMN biometric.heart_rate; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.biometric.heart_rate IS 'The heart rate of the patient in beats per minute';


--
-- TOC entry 3915 (class 0 OID 0)
-- Dependencies: 198
-- Name: COLUMN biometric.blood_pressure; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.biometric.blood_pressure IS 'The blood pressure of the patient in mmHg';


--
-- TOC entry 199 (class 1259 OID 20996)
-- Name: emotion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.emotion (
    id uuid DEFAULT public.gen_random_uuid() NOT NULL,
    patient_id uuid NOT NULL,
    dominant_emotion character varying(255) NOT NULL,
    neutral numeric,
    anger numeric,
    happiness numeric,
    surprise numeric,
    sadness numeric,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone
);


ALTER TABLE public.emotion OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 21004)
-- Name: game; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game (
    id uuid DEFAULT public.gen_random_uuid() NOT NULL,
    game_id uuid NOT NULL,
    description character varying(255) NOT NULL,
    patient_id uuid NOT NULL,
    left_hand_score integer,
    right_hand_score integer,
    time_played integer,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone
);


ALTER TABLE public.game OWNER TO postgres;

--
-- TOC entry 3916 (class 0 OID 0)
-- Dependencies: 200
-- Name: COLUMN game.time_played; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.game.time_played IS 'Game time played in seconds';


--
-- TOC entry 201 (class 1259 OID 21009)
-- Name: gyros; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gyros (
    id uuid DEFAULT public.gen_random_uuid() NOT NULL,
    gyro_id uuid NOT NULL,
    description character varying(255) NOT NULL,
    patient_id uuid NOT NULL,
    x numeric,
    y numeric,
    z numeric,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone
);


ALTER TABLE public.gyros OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 21017)
-- Name: medication; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medication (
    id uuid DEFAULT public.gen_random_uuid() NOT NULL,
    patient_id uuid NOT NULL,
    device_id uuid NOT NULL,
    scheduled_time character varying(255) NOT NULL,
    response boolean,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone
);


ALTER TABLE public.medication OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 21022)
-- Name: personal_check_in; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.personal_check_in (
    id uuid DEFAULT public.gen_random_uuid() NOT NULL,
    patient_id uuid NOT NULL,
    category character varying(255) NOT NULL,
    value character varying(255),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone
);


ALTER TABLE public.personal_check_in OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 21030)
-- Name: test; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.test (
    id uuid DEFAULT public.gen_random_uuid() NOT NULL,
    test_id uuid NOT NULL,
    description character varying(255) NOT NULL,
    patient_id uuid NOT NULL,
    test_score integer,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone
);


ALTER TABLE public.test OWNER TO postgres;

--
-- TOC entry 3765 (class 2606 OID 21036)
-- Name: accels accels_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accels
    ADD CONSTRAINT accels_pkey PRIMARY KEY (id);


--
-- TOC entry 3769 (class 2606 OID 21038)
-- Name: biometric biometric_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.biometric
    ADD CONSTRAINT biometric_pkey PRIMARY KEY (id);


--
-- TOC entry 3775 (class 2606 OID 21040)
-- Name: gyros gyros_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gyros
    ADD CONSTRAINT gyros_pkey PRIMARY KEY (id);


--
-- TOC entry 3783 (class 2606 OID 21042)
-- Name: test test_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_pkey PRIMARY KEY (id);


--
-- TOC entry 3785 (class 2606 OID 21044)
-- Name: test unique; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT "unique" UNIQUE (id);


--
-- TOC entry 3777 (class 2606 OID 21046)
-- Name: gyros unique_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gyros
    ADD CONSTRAINT unique_id UNIQUE (id);


--
-- TOC entry 3771 (class 2606 OID 21048)
-- Name: biometric unique_id_constraint; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.biometric
    ADD CONSTRAINT unique_id_constraint UNIQUE (id);


--
-- TOC entry 3767 (class 2606 OID 21050)
-- Name: accels unique_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accels
    ADD CONSTRAINT unique_pkey UNIQUE (id);


--
-- TOC entry 3773 (class 2606 OID 21052)
-- Name: emotion unique_pkey_emotion; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emotion
    ADD CONSTRAINT unique_pkey_emotion UNIQUE (id);


--
-- TOC entry 3779 (class 2606 OID 21056)
-- Name: medication unique_pkey_medication; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medication
    ADD CONSTRAINT unique_pkey_medication UNIQUE (id);


--
-- TOC entry 3781 (class 2606 OID 21054)
-- Name: personal_check_in unique_pkey_personal; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.personal_check_in
    ADD CONSTRAINT unique_pkey_personal UNIQUE (id);


--
-- TOC entry 3912 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM rdsadmin;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2020-04-02 15:10:42 EDT

--
-- PostgreSQL database dump complete
--

