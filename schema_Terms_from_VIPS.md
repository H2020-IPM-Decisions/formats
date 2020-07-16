# Json-LD Documentation

## Sources documentations

Json-ld: <https://json-ld.org/>
Json-ld documentation: <https://json-ld.org/learn.html>
schema: <http://www.schema.org>

## JSON-LD Context creation

1. DSS_schema context (VIPS): DSS_schema.jsonld
2. DSS_model context: DSS_model.jsonld

## Terms definition

### Properties description can be issue from schema

| properties | Type | reference | description |
|--|--|--|--|
| address | Text | schema:streetAddress | The street address. For example, 1600 Amphitheatre Pkwy. |
| author | Text | schema:author | The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably. |
| city | Text | schema:City | A city or town. |
| countries | Text | schema:countriesSupported | schema:Thing | Countries for which the application is supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code. |
| country | Text | schema:addressCountry | The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code. |
| description | Text | schema:description | A description of the item. |
| email | Text | schema:email | Email address. |
| id | PropertyValue, URL or Text | schema:identifier | The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See background notes for more details |
| keywords | Text | schema:Keywords | Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas. |
| languages | Text | schema:availableLanguage | A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard |
| name | Text | schema:name | schema:Thing | The name of the item.(organisation,model,author) |
| organization | Text | schema:affiliation | An organization that this person is affiliated with. For example, a school/university, a club, or a team. |
| organization | Organization | schema:Organisation | An organization such as a school, NGO, corporation, club, etc. |
| postal_code | Text | schema:postalCode | The postal code. For example, 94043. |
| type | Object Type | schema | The object type (e.g. ONTHEFLY). |
| url | URL | schema:url | schema:Thing | URL of the item. |
| version | Number or Text | schema:version | The version of the CreativeWork embodied by a specified resource. |

### Properties description can be issue from ipmdecision

| properties | Type | reference | description |
|--|--|--|--|
| citation | URL | ipmdecision:citation | List of DOI about model |
| content_type |  | ipmdecision:form_method | Regular forms: application/x-www-form-urlencoded , Regular forms with files: multipart/form-data |
| crops | List | ipmdecision:crops | list of crop using EPPO code. See code on <https://gd.eppo.int/> |
| description_URL | URL | ipmdecision:description_URL | url of documentation about model |
| endpoint | URL | ipmdecision:endpoint | URL where your service can be accessed by a client application. |
| execution | execution | ipmdecision:execution | execution of model |
| form_method | Text | ipmdecision:form_method | The formmethod attribute specifies which HTTP method to use when sending the form-data,The form-data can be sent as URL variables (with method="get") or as HTTP post (with method="post") definition trouvé dans <https://www.w3schools.com/tags/att_button_formmethod.asp> |
| input_schema | schema | ipmdecision:input_format | The input template should adhere to the JSON Schema standard: <https://json-schema.org/> |
| intput | Input | ipmdecision:input | datatype input in the model |
| DSS_Model | DSS_Model | ipmdecision:DSS_Model | model Catalog with their descriptions |
| output |  | ipmdecision:output | Definition of the result parameters specific for this DSS model |
| parameter_code | Number | ipmdecision:parameter_code | is an identifier for described variable parameter_code id is on <https://github.com/H2020-IPM-Decisions/formats/blob/master/weather_data/> |
| pests | List | ipmdecision:pests | list of a pest using EPPO code See code on <https://gd.eppo.int/> |
| result_parameters |  | ipmdecision:result_parameters | Definition of the result parameters specific for this DSS model |
| type_of_decision | Text | ipmdecision:type_of_decision | indicate the type of decision for user |
| type_of_output | Text | ipmdecision:type_of_output | indicate the type of output |
| valid_spatial | valid_spatial | ipmdecision:valid_spatial | spatial validation of model |
| warning_status_interpretation | Text | ipmdecision:warning_status_interpretation | Definition of the warning_station_interpretation specific for this DSS model |
| weather | Datatype | ipmdecision:weather | weather data for parameter_code is described in <https://github.com/H2020-IPM-Decisions/formats/blob/master/weather_data/weather_parameters_draft_v2.yaml> |
| interval | INT | ipmdecision:interval | Sampling interval in second |
| title | Text|ipmdecision:title|Title of the graph or parameter|

>[!NOTE]
>I'm not sure about the property for:
>
> * id
> * languages
> * valid_spatial
>
>Problem with organization first describe organization et in author describe affiliation
> Datatype: schema
