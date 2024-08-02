--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3 (Debian 16.3-1.pgdg120+1)
-- Dumped by pg_dump version 16.3 (Debian 16.3-1.pgdg120+1)

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
-- Name: language; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.language AS ENUM (
    'RU',
    'EN'
);


ALTER TYPE public.language OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: achievements; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.achievements (
    name character varying NOT NULL,
    number_points integer NOT NULL,
    description text NOT NULL,
    id uuid NOT NULL
);


ALTER TABLE public.achievements OWNER TO postgres;

--
-- Name: COLUMN achievements.name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.achievements.name IS 'Название достижения';


--
-- Name: COLUMN achievements.number_points; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.achievements.number_points IS 'Количество баллов за достижения';


--
-- Name: COLUMN achievements.description; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.achievements.description IS 'Описание достижения';


--
-- Name: COLUMN achievements.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.achievements.id IS 'Уникальный идентификатор';


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    name character varying NOT NULL,
    language public.language NOT NULL,
    id uuid NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: COLUMN users.name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.users.name IS 'Имя пользователя';


--
-- Name: COLUMN users.language; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.users.language IS 'Выбранный пользователем язык';


--
-- Name: COLUMN users.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.users.id IS 'Уникальный идентификатор';


--
-- Name: users_achievements; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_achievements (
    user_id uuid NOT NULL,
    achievement_id uuid NOT NULL,
    date_on timestamp without time zone NOT NULL
);


ALTER TABLE public.users_achievements OWNER TO postgres;

--
-- Name: COLUMN users_achievements.date_on; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.users_achievements.date_on IS 'Дата выдачи достижения';


--
-- Data for Name: achievements; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.achievements (name, number_points, description, id) FROM stdin;
Сердце на рукаве|A heart on a sleeve	150	Отреагируйте на что-либо на GitHub с помощью эмодзи ❤️|React to something on GitHub with an emoji ❤️	3d41dbf7-eff3-4c90-b5ad-12ddcee1b232
Открытый источник|Open Sourcerer	150	Вы сделали PR в несколько общедоступных репозиториев и эти PR были смёржены|You made PR to several publicly available repositories and those PR were smirked away	5847d89a-8b9a-46d6-b5f0-483e393c5461
Звездная болезнь|Starstruck	50	Созданный вами репозиторий должен получить 16 звёзд или больше|The repository you created should receive 16 stars or more	8e37bd42-f2c8-465f-a326-69b66bcdc2da
Контрибьютор в арктическое хранилище|Arctic Code Vault Contributor	1000	Ваш код был включён в программу 2023 GitHub Archive Program. Выдавался за хотя бы 1 случай вклада|Your code was included in the 2023 GitHub Archive Program. Issued for at least 1 case of contribution	54a40af7-dad6-4126-94b9-9c3ccc4cf5a4
Быстрый выстрел|Quickdraw	250	Выдаётся, если вы хотя бы один раз закрыли issue или смёржили pull request в течение 5 минут после открытия|Issued if you have closed an issue or smirked a pull request at least once within 5 minutes of opening it	4df1d7af-8332-434a-92b3-0f83bf93baf6
Экстраординарная пара|Pair Extraordinaire	400	Был смёржен один или несколько pull request, который вы делали в соавторстве с другими разработчиками|One or more pull requests that you co-authored with other developers have been smashed	1561a9c9-9cde-4cac-9db2-1649e8fc233a
Вытащить акулу|Pull Shark	120	Было принято (смёржено) два открытых вами pull request-а (или больше)|Two (or more) pull requests you opened were accepted (smirked)	c6a64c3f-b387-4c0e-bae7-a1c1fd558b9c
Мозг галактики|Galaxy Brain	200	Автор дискуссии принял два (или больше) ваших ответа (нажал Mark as answer)|The author of the discussion accepted two (or more) of your responses (clicked Mark as answer)	ab0900a7-d3e9-4236-a7ec-ddae23dfc753
Живем только раз|YOLO	50	Выдаётся, если хотя бы один ваш pull request был принят без замечаний (автор не написал ни одного треда и смёржил правки)|Issued if at least one of your pull requests has been accepted without comments (the author has not written a single track and has smirked the edits)	3449e0f6-2c95-4bb4-9091-c8ca60eb36a0
Общественный спонсор|Public Sponsor	500	Выдаётся, если вы хотя бы один раз спонсировали opensource-проект или разработчика на GitHub|Issued if you have sponsored an opensource project or developer on GitHub at least once	89489bc6-57e2-4dd0-b927-6a943e2ee653
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
8d2b8d633509
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (name, language, id) FROM stdin;
Иван	RU	d7b62fbd-63d8-491e-ba08-12d8e403b54a
Ivan	EN	891aa403-356e-4db3-837e-4cfa4202647f
Алина	RU	7460eba7-4088-40a0-b305-0b924eab214a
Alex	EN	419272dd-762d-4345-a323-d5e1d0c32383
Сергей	RU	19b65ea6-d83a-497b-93b9-c046d638eb37
Алексей	RU	458c50e8-d573-4ec8-99ad-5f4ccc6b855b
Владимир	RU	86ead66c-ddbc-46e2-b451-bcef6212f78c
Роман	RU	bb205224-e362-4438-b58f-fd171a84f1d4
Дарина	RU	c9788b61-9291-45ea-9c4c-37e4a5c73cd5
Mary	EN	a5faccdd-2144-4584-9728-172a188d8e41
Ida	EN	34d3a604-6e4d-4c45-94a1-9fb9be981acf
Robert	EN	b8b9b088-d830-4934-8efd-fe2a43f5a4e6
Мария	RU	a8d0660b-e05b-4528-8b05-e8f6cf91aec4
Илья	RU	ec6efab8-0816-4dc3-a397-234d1a084796
Даниил	RU	9dd4ace1-5535-4e3d-85ae-afe7e55a7c6d
Ангелина	RU	9fc5ff12-a47f-48de-b1cf-50ad279ee722
Ярослав	RU	a232886e-2223-4c5b-a4ed-c1c0b2862e92
Willie	EN	537ab25d-7216-4230-adb9-56d04f45fefd
Nicole	EN	26ea908d-bd16-43e9-9ce3-b82fcd1c303c
Clara	EN	7d36544c-f868-4f62-aee0-823c0d050001
\.


--
-- Data for Name: users_achievements; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_achievements (user_id, achievement_id, date_on) FROM stdin;
d7b62fbd-63d8-491e-ba08-12d8e403b54a	5847d89a-8b9a-46d6-b5f0-483e393c5461	2024-07-30 21:48:09.021
d7b62fbd-63d8-491e-ba08-12d8e403b54a	8e37bd42-f2c8-465f-a326-69b66bcdc2da	2024-07-30 21:48:09.021
d7b62fbd-63d8-491e-ba08-12d8e403b54a	4df1d7af-8332-434a-92b3-0f83bf93baf6	2024-07-30 21:48:09.021
d7b62fbd-63d8-491e-ba08-12d8e403b54a	1561a9c9-9cde-4cac-9db2-1649e8fc233a	2024-07-30 21:48:09.021
d7b62fbd-63d8-491e-ba08-12d8e403b54a	c6a64c3f-b387-4c0e-bae7-a1c1fd558b9c	2024-07-30 21:48:09.021
d7b62fbd-63d8-491e-ba08-12d8e403b54a	ab0900a7-d3e9-4236-a7ec-ddae23dfc753	2024-07-30 21:48:09.021
d7b62fbd-63d8-491e-ba08-12d8e403b54a	3449e0f6-2c95-4bb4-9091-c8ca60eb36a0	2024-07-30 21:48:09.021
d7b62fbd-63d8-491e-ba08-12d8e403b54a	54a40af7-dad6-4126-94b9-9c3ccc4cf5a4	2024-07-30 21:48:09.021
c9788b61-9291-45ea-9c4c-37e4a5c73cd5	8e37bd42-f2c8-465f-a326-69b66bcdc2da	2024-07-30 21:48:09.021
a5faccdd-2144-4584-9728-172a188d8e41	c6a64c3f-b387-4c0e-bae7-a1c1fd558b9c	2024-07-30 21:48:09.021
a5faccdd-2144-4584-9728-172a188d8e41	ab0900a7-d3e9-4236-a7ec-ddae23dfc753	2024-07-30 21:48:09.021
c9788b61-9291-45ea-9c4c-37e4a5c73cd5	ab0900a7-d3e9-4236-a7ec-ddae23dfc753	2024-07-30 21:48:09.021
d7b62fbd-63d8-491e-ba08-12d8e403b54a	3d41dbf7-eff3-4c90-b5ad-12ddcee1b232	2024-07-31 21:48:09.021
d7b62fbd-63d8-491e-ba08-12d8e403b54a	89489bc6-57e2-4dd0-b927-6a943e2ee653	2024-07-25 12:48:09.021
ec6efab8-0816-4dc3-a397-234d1a084796	8e37bd42-f2c8-465f-a326-69b66bcdc2da	2024-07-25 12:48:09.021
\.


--
-- Name: achievements achievements_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.achievements
    ADD CONSTRAINT achievements_name_key UNIQUE (name);


--
-- Name: achievements achievements_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.achievements
    ADD CONSTRAINT achievements_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: users_achievements users_achievements_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_achievements
    ADD CONSTRAINT users_achievements_pkey PRIMARY KEY (user_id, achievement_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users_achievements users_achievements_achievement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_achievements
    ADD CONSTRAINT users_achievements_achievement_id_fkey FOREIGN KEY (achievement_id) REFERENCES public.achievements(id);


--
-- Name: users_achievements users_achievements_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_achievements
    ADD CONSTRAINT users_achievements_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

