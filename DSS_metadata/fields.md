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
|               | DSS_id            | package    | Model_id                                           | package identifier                                                                   |
|               | DSS_name          | name       | name                                               | package name                                                                         |
|               | public_URL        | url        |                                                    | url to platform access                                                               |
|               | contact_email     | authors    | authors                                            | contact mail                                                                         |
|               | login_requirement | X          | X                                                  | boolean                                                                              |
|               | DSS_owner         | Institutes | Institution                                        | Owner description equivalent to institute (name, country, address,postal code, city) |
|               | languages         | X          |                                                    | platform language                                                                    |
|               | X                 | alias      | X                                                  | Alias for compatibility                                                              |
|               | X                 | X          | version                                            | package version                                                                      |
|               | X                 | X          | release                                            |                                                                                      |
|               | X                 | X          | base language                                      | code source language                                                                 |
|               | X                 | X          | Licence                                            | package licence                                                                      |
|               | X                 | X          | References                                         | Publication                                                                          |
|               | X                 | X          |                                                    |                                                                                      |
|               | DSS_model_name    |            | title                                              | model name                                                                           |
|               | DSS_model_id      |            | model_id                                           | model identifier                                                                     |
|               | pests             |            |                                                    | name (EPPO code)                                                                     |
|               | crops             |            |                                                    | name (EPPO code)                                                                     |
|               | type_of_decision  |            |                                                    | Short-term tactical                                                                  |
|               | type_of_output    |            | output                                             |                                                                                      |
|               | Description_URL   |            |                                                    | url for model                                                                        |
|               | Description       |            | abstract                                           | short model description                                                              |
|               | Input             |            | Input                                              |                                                                                      |
|               | How_to_run        |            | Algorithme, initialisation, fonction, parameterset |                                                                                      |
|               |         |            | Testeset |                                                                                      |

>[!NOTE]
>Je pense qu'il y a plein de chose qui peuvent être enlever comme input How_to_run ect qui sont repris dans un tableau plus bas

#### DSS INPUT

| selected name | VIPS                       | OpenAlea | Crop2ML           | Description                                                                 |
|---------------|----------------------------|----------|-------------------|-----------------------------------------------------------------------------|
|               | weather, field_observation |          | variablecategory  | indicate the type of variable (state, a rate or an “auxiliary”) variable    |
|               | parameter code             |          | name              | for DSS name of variable, unit, mean                                        |
|               | interval                   |          |                   |                                                                             |
|               | spiecies                   |          |                   | name EPPO                                                                   |
|               |                            |          | description       | short description of input                                                  |
|               |                            |          | parametercategory | indicate the type of parameter (constant, species, soil and genotypic       |
|               |                            |          | datatype          | indication of the type of variable STRING, STRING LIST, STRING ARRAY ect... |
|               |                            |          | min, max          | range of value                                                              |
|               |                            |          | unit              | unit Ontology developed by WUR                                              |
|               |                            |          | uri               |                                                                             |
|               |                            |          | input_type        | indication of type of input (parameter or variable)                         |

#### DSS Output

| selected name | VIPS             | OpenAlea | Crop2ML     | Description                     |
|---------------|------------------|----------|-------------|---------------------------------|
|               | type_of_output   |          |             | type of output (Risk indicator) |
|               | type_of_decision |          |             | type of output (Risk indicator) |
|               |                  | name     | name        |                                 |
|               |                  |          | description |                                 |
|               |                  |          | min         | min value                       |
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
|               |              |             | Algorithme     | name, language, filename                             |
|               |              |             | Initialisation | name, language, filename                             |
|               |              | node module |                | name of the python module containing fonction/ class |
|               |              | node class  |                | name of the component function/class                 |

>[!NOTE]
>Faut il detailler algorithme et initialisation à part?

#### DSS Parameterset

| selected name | VIPS | OpenAlea | Crop2ML     | Description                 |
|---------------|------|----------|-------------|-----------------------------|
|               |      |          | name        | name of parameterset        |
|               |      |          | description | description of parameterset |
|               |      |          | uri         |                             |
|               |      |          | param       | name and value of parameter |

#### DSS Testset

| selected name | VIPS | OpenAlea | Crop2ML      | Description                                       |
|---------------|------|----------|--------------|---------------------------------------------------|
|               |      |          | name         |                                                   |
|               |      |          | parameterset |                                                   |
|               |      |          | description  |                                                   |
|               |      |          | uri          |                                                   |
|               |      |          | Test         | inputvalue (name), output value (name, precision) |

>[!CAUTION]
>A partir de la il s'agit des anciens tableau je pense que l'on pourra les supprimer

#### 4.1.1 VIPS

| VIPS-element      | VIPS-description                                                                   |
|-------------------|------------------------------------------------------------------------------------|
| DSS_id            | package identifiers                                                                |
| DSS_name          | model name                                                                         |
| public_URL        | url to platform access                                                            |
| contact_email     | contact mail                                                                       |
| login_requirement | boolean                                                                            |
| DSS_owner         | Owner description equivalent to institute (name, contry, adress,postal code, city) |
| languages         | plateform language                                                                 |

#### 4.1.2 Crop2ML

| Crop2ML-element | Crop2ML-description                              |
|-----------------|--------------------------------------------------|
| Description     | Title, Authors, Institution, Reference, Abstract |
|                 |                                                  |

#### 4.1.3 OpenAlea

| OpenAlea-element | Openalea-description                    |
|------------------|-----------------------------------------|
| _init_.py        | Contains python package declaration     |
| _wrealea_.py     | contains openalea component declaration |
| python modules   |                                         |

### 4.2 Model/package informations

| VIPS-element     | VIPS-description                                                                                                                              |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| DSS_model_name   | name                                                                                                                                          |
| DSS_model_id     | id model                                                                                                                                      |
| pests            | name EPPO code for pest                                                                                                                       |
| crops            | name EPPO code for crops                                                                                                                      |
| type_of_decision | short time technical                                                                                                                          |
| type_of_output   | risk indicator                                                                                                                                |
| Description_URL  | URL contains model descriptions, Interpretation status, technical usage (todo), sample configuration                                          |
| Description      | Model decription (abstract)                                                                                                                   |
| Input            | Input variable (weather, field observation) and parameter (for weather: parameter code, interval, for field observation: spiecies EPPO code?) |
| How_to_run       | type ?, Endpoint (url), Form_method (get or post), content_type (json application), input_schema                                              |

#### 4.2.1 VIPS

| VIPS-element | VIPS-description |
|--|--|
| DSS_model_name | name |
| DSS_model_id | id model |
| pests | name EPPO code for pest |
| crops | name EPPO code for crops |
| type_of_decision | short time technical |
| type_of_output | risk indicator |
| Description_URL | URL contains model descriptions, Interpretation status, technical usage (todo), sample configuration |
| Description | Model decription (abstract) |
| Input | Input variable (weather, field observation) and parameter (for weather: parameter code, interval, for field observation: spiecies EPPO code?) |
| How_to_run |type ?, Endpoint (url), Form_method (get or post), content_type (json application), input_schema|

#### 4.2.2 Crop2ML

| Crop2ML-element | Crop2ML description |
|--|--|
| ModelUnit | The root of an atomic model in Crop2ML which make the difference from a composite model. |
| Description | Title, authors, Institutions, References, Abstract |
| Inputs | A list of inputs characterized by their names,. Its input variables are related to climate, soil and cropping system |
||name, description
||variablecategory (state, rate, auxillary) or parametercategory (constant, species, soil),genotypic)|
|| datatype (type of variable (string, data, double,int boolean))|
|| min, max, default, uri|
||inputtype (variable, parameter)|
| Outputs | A list of outputs defining the processes involved, the variables whose dynamics we want to observe. |
|ModelComposition|Model (name,filename), Link( input link (target, source), internallink (target, source), outputlink(source, target)|
| Initialization | A process used to attribute an initial value to the state, rate and auxiliary variables. |
||name, language, filename|
| Function | A service called by an atomic or composite model for a specific action. |
||name|
||language|
||filename|
| Algorithm | The description of the behaviour of the model made by the mathematical relationship between the inputs and the outputs with some control structure. |
||language|
||filename|
||plateform|
| Parametersets | Some sets of parameters which are invariant and used for the simulation of the models. |
||Parameterset (name, description, uri)|
||param (name, values)|
| Testsets | Set of model configuration used to compare estimated and desired outputs |
||Testset (name, parameterset, description, uri)|
||Test( name,Inputvalue (name, value), OutputValue(name, precision,value))

#### 4.2.3 OpenAlea

| OpenAlea-element | Openalea-Description |
|--|--|
| _wralea_.py | contains package meta_informations and component declaration |
| _wralea_.py (meta-information) | name, version, licence, authors,institutes, url, alias (list of alias name for the package),editable (allows or not edit the package) |
| _wralea_.py (components) | contains Factory declaration and inputs/outputs port |
| _wralea_.py(components- factory)| _all_: global variable containing the list of variable name pointing to a factory,
| |name: component string id|
| |description: description string, category: string to classify the components|  
| |nodemodule: name of the python module containing fonction/ class|
| |nodeclass: name of the component function/class|
| |inputs[optional] : the input ports description (a list of dict)|
| |outputs[optional] : the output ports description (a list of dict)
| |widgetmodule[optional] : the name of the python module (without .py) containing the widget class|
| |widgetclass[optional] : the name of the widget class (as a string)|
| |lazy[optional] : The node support lazy evaluation|
| | alias: list of alias names |
| _wralea_.py(components- inputs/outputs port) | name : the port name|
||interface : interface class (or instance) to describe the port|
|| value: default value, desc: help string|
||label: port widget title|
||showwidget: display the corresponding interface widget, hide: hide port|
