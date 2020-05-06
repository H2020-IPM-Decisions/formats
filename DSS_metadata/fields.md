# Fields

## 1. General information about DSS

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

## 2. Specific model description

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

## 3 graphical comparison of VIPS OpenAlea crop2ML models

![Getting Started](./VIPS-crop2ml_openalea.jpg)

**html link:**
file:///C:/Users/mlabadie/Documents/Travail/Cirad/IPM-Project/formats/DSS_metadata/VIPS-crop2ml_openalea.html

## 4. Comparison table VIPS OpenAlea, cropm2ML

The information was found on the following sites:

- VIPS: <https://github.com/H2020-IPM-Decisions/formats/blob/master/DSS_metadata/VIPS.yaml>
- Crop2ML: <https://crop2ml.readthedocs.io/en/latest/>
- Openalea: <http://openalea.gforge.inria.fr/dokuwiki/doku.php?id=documentation:component:how_to_declare_logical_components>

**Global information / Meta-information:**

| VIPS-element       | VIPS-description                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| DSS_id            | model identifiant                                                                  |
| DSS_name          | model name                                                                         |
| public_URL        | url to plateform access                                                            |
| contact_email     | contact mail                                                                       |
| login_requierment | boolean                                                                            |
| DSS_owner         | Owner description equivalent to institute (name, contry, adress,postal code, city) |
| languages         | model or platform languages ?                                                      |

| Crop2ML-element | Crop2ML-description                              |
|-----------------|--------------------------------------------------|
| Description     | Title, Authors, Institution, Reference, Abstract |
|                 |                                                  |

OpenAlea-element|
**Model informations:**

| VIPS-element | VIPS-description |
|--|--|
| DSS_model_name | name |
| DSS_model_id | id model |
| pests | EPPO code for pest |
| crops | EPPO code for crops |
| type_of_decision | short time technical |
| type_of_output | risk indicator |
| Description_URL | URL contains model descriptions, Interpretation status, technical usage (todo), sample configuration |
| Description | Model decription (abstract) |
| Input | Input variable (weather, field observation) and parameter (for weather: parameter code, interval, for field observation: spiecies EPPO code?) |
| How_to_run | Contain type, Endpoint, Form_method, content_type, input_schema |

| Crop2ML-element | Crop2ML description |
|--|--|
| ModelUnit | The root of an atomic model in Crop2ML which make the difference from a composite model. |
| Description | Title, authors, Institutions, References, Abstract |
| Inputs | A list of inputs characterized by their names,. Its input variables are related to climate, soil and cropping system |
| Outputs | A list of outputs defining the processes involved, the variables whose dynamics we want to observe. |
| Initialization | A process used to attribute an initial value to the state, rate and auxiliary variables. |
| Function | A service called by an atomic or composite model for a specific action. |
| Algorithm | The description of the behaviour of the model made by the mathematical relationship between the inputs and the outputs with some control structure. |
| Parametersets | Some sets of parameters which are invariant and used for the simulation of the models. |
| Testsets | Set of model configuration used to compare estimated and desired outputs |
