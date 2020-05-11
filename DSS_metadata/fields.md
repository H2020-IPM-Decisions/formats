# Model representation : Metadata and Fields

Description of the representation of formats for Model in VIPS, OpenAlea and Crop2ML.
VIPPS is designed to represent DSS, OpenAlea is more general, and Crop2ML focus on cropo model.

## General information about DSS

A DSS is represented as a set of models and meta-information.

- [ ] DSS_id:
- [ ] DSS_name:
- [ ] Public URL:
- [ ] Contact_email:
- [ ] login_required: (true or false)
- [ ] DSS_owner:
  - [ ] name:
  - [ ] country:
  - [ ] adress:
  - [ ] postal_code:
  - [ ] city:
  - [ ] Languages:

## Specific model description about DSS

There may be many DSS models per DSS

They should have their separate list entry

We use EPPO codes (<https://gd.eppo.int/)>

For pests and crops We use these parameters/codes for weather data: <https://github.com/H2020-IPM-Decisions/formats/blob/master/weather_data/weather_parameters_draft_v1.txt>

- DSS models:
  - [ ] DSS_model_name:
  - [ ] DSS_model_id:
  - [ ] pests: (code EPPO)
  - [ ] Crops: (Code EPPO)
  - [ ] Type_of_decision:
  - [ ] Type_of_output:
  - [ ] Description_URL:
  - [ ] Description:
  - [ ] Input:
    - [ ] Weather
      - [ ] parameter_code:
      - [ ] interval:
    - [ ] Field_observation:
      - [ ] species: (code EPPO)
  - [ ] How_to_run:
    - [ ] Type
    - [ ] Endpoint:
    - [ ] Form_method: (get or post)
    - [ ] Content_type:
    - [ ] Input_schema:

## Graphical comparison of VIPS, OpenAlea, and Crop2ML models

![Getting Started](./VIPS-crop2ml_openalea.jpg)

## Comparison table VIPS, OpenAlea, cropm2ML

The information was found on the following sites:

- VIPS: <https://github.com/H2020-IPM-Decisions/formats/blob/master/DSS_metadata/VIPS.yaml>
- Crop2ML: <https://crop2ml.readthedocs.io/en/latest/>
- Openalea: <http://openalea.gforge.inria.fr/dokuwiki/doku.php?id=documentation:component:how_to_declare_logical_components>

### 4.1 Global information / Meta-information

#### Some definitions

- **Package** / **DSS**: A package (or a DSS) represents a container of **Models** with meta-information.
- **Model**: a computational unit that implement a given contract with explicit inputs and outputs.

#### DSS Description

| selected name | VIPS              | OpenAlea   | Crop2ML                                            | Description                                                                          |
|---------------|-------------------|------------|----------------------------------------------------|--------------------------------------------------------------------------------------|
|               | DSS_id            | package (a.b.c)   | Model_id                                           | package identifier (**use of real identifier or uri**?)                                                                  |
|               | DSS_name          | name (same as id)      | name                                               | package name                                                                         |
|               | public_URL        | url        |                                                    | public url use for documentation                                                               |
|               | contact_email     | authors    | authors                                            | contact mail                                                                         |
|               | login_requirement | X          | X                                                  | **Too restrictive?** Authorisation: login, public, ...                                                                               |
|               | DSS_owner         | Institutes | Institution                                        | List of Owner description equivalent to institute (name, country, address,postal code, city, url) |
|               | languages         | X          |                                                    | platform language (english)                                                                   |
|               | X                 | alias      | X                                                  | Alias for compatibility. DSS name may change through time.                                                              |
|               | X                 | version          | version                                            | package version                                                                      |
|               | X                 | X          | release                                            |                                                                                      |
|               | X                 | X          | base language                                      | code source language                                                                 |
|               | X                 | X          | Licence                                            | package licence                                                                      |
|               | X                 | description          | References                                         | long description                                                                          |
|               | X                 | citation          |                                                    |  Publication / doi                                                                                    |

> Look a PyPi fields to declare a package in Python. 
> Add for instance classifiers 

#### Model description
A model belongs to a package / DSS.
A Package will contains one or several models.


| selected name | VIPS              | OpenAlea   | Crop2ML                                            | Description                                                                          |
|---------------|-------------------|------------|----------------------------------------------------|--------------------------------------------------------------------------------------|
|               | DSS_model_id      |            | model_id                                           | model identifier                                                                     |
|               | DSS_model_name    |            | title                                              | model name                                                                           |
|               | pests             |  category  |                                                    | name (EPPO code)                                                                     |
|               | crops             |  category  |                                                    | name (EPPO code)                                                                     |
|               | type_of_decision  |  category  |                                                    | Short-term tactical                                                                  |
|               | type_of_output    |   outputs  | output                                             |                                                                                      |
|               | Description_URL   |      X     |    X                                               | url for model                                                                        |
|               | Description       | descrption | abstract                                           | short model description                                                              |
|               | Input             |    inputs  | Input                                              |                                                                                      |
|               | How_to_run        | Python module / class | Algorithm, initialisation, fonction |                                                                                      |
|               |         |            | Testeset |                                                                                      |

>[!NOTE]
>Je pense qu'il y a plein de chose qui peuvent être enlever comme input How_to_run ect qui sont repris dans un tableau plus bas

#### DSS INPUT

| selected name | VIPS                       | OpenAlea | Crop2ML           | Description                                                                 |
|---------------|----------------------------|----------|-------------------|-----------------------------------------------------------------------------|
|               | weather, field_observation |          | variablecategory  | indicate the type of variable (state, a rate or an “auxiliary”) variable    |
|               | parameter code             | name     | name              | for DSS name of variable, unit, mean                                        |
|               | interval                   |interface |  min, max, defaul | range of values                                                                            |
|               | species                    |          |                   | name EPPO                                                                   |
|               |                            |   desc   | description       | short description of input                                                  |
|               |                            |          | variablecategory | indicate the type of parameter (constant, species, soil and genotypic       |
|               |                            | interface| datatype          | indication of the type of variable STRING, STRING LIST, STRING ARRAY ect... |
|               |                            |          | unit              | unit Ontology developed by WUR                                              |
|               |                            |          | uri               |                                                                             |
|               |                            |          | input_type        | indication of type of input (parameter or variable)                         |

#### DSS Output

| selected name | VIPS             | OpenAlea | Crop2ML     | Description                     |
|---------------|------------------|----------|-------------|---------------------------------|
|               | type_of_output   |          |             | type of output (Risk indicator) |
|               | type_of_decision |          |             | type of output (Risk indicator) |
|               |                  | name     | name        |                                 |
|               |                  | desc     | description |                                 |
|               |                  | interface| min         | min value                       |
|               |                  | interface| min         | min value                       |
|               |                  |          | max         | max value                       |
|               |                  |          | uri         |                                 |

#### DSS how_to_run/Algoritme-initialisation-Function

| selected name | VIPS         | OpenAlea    | Crop2ML        | Description                                          |
|---------------|--------------|-------------|----------------|------------------------------------------------------|
|               | type         |             |                |                                                      |
|               | Endpoint     |             |                | url                                                  |
|               | form_method  |             |                | post or get                                          |
|               | content_type |             |                | application/json                                     |
|               | input_schema |             |                |                                                      |
|               |              |             | Algorithm      | name, language, filename                             |
|               |              |             | Initialisation | name, language, filename                             |
|               |              | node module |                | name of the python module containing fonction/ class |
|               |              | node class  |                | name of the component function/class                 |




