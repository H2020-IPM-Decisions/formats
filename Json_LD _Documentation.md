# Json-LD Documentation

## What is JSON-LD (JSON-Linkdata)

Linked Data [LINKED-DATA] is a way to create a network of standards-based machine interpretable data across different documents and Web sites. It allows an application to start at one piece of Linked Data, and follow embedded links to other pieces of Linked Data that are hosted on different sites across the Web.

JSON-LD is a lightweight syntax to serialize Linked Data in JSON [RFC8259]. Its design allows existing JSON to be interpreted as Linked Data with minimal changes. JSON-LD is primarily intended to be a way to use Linked Data in Web-based programming environments, to build interoperable Web services, and to store Linked Data in JSON-based storage engines. Since JSON-LD is 100% compatible with JSON, the large number of JSON parsers and libraries available today can be reused. In addition to all the features JSON provides.

JSON-LD introduces:
* a universal identifier mechanism for JSON objects via the use of IRIs,
* a way to disambiguate keys shared among different JSON documents by mapping them to IRIs via a context,
* a mechanism in which a value in a JSON object may refer to a resource on a different site on the Web,
* the ability to annotate strings with their language,
* a way to associate datatypes with values such as dates and times,
and a facility to express one or more directed graphs, such as a social network, in a single document.


>**Sources documentations**
>* json-ld: <https://json-ld.org/>   
>* json-ld documentation: <https://json-ld.org/learn.html>    
>* json-ld syntax: <https://www.w3.org/TR/json-ld/>  


## JSON-LD Context for IPM-Decision

1. DSS_schema context: DSS_schema.jsonld, contains meta-information for DSS
2. DSS_model context: DSS_model.jsonld, contains context for each DSS_Model/package

|Note: These contexts were difined using mainly schema.org context. Some Term provided from codemeta and some new Term specific to ipmdecision are add. All Terms were difined below in term definition section.|
|-|

An example  using these contexts are available:
* For VIPS: [DSS_metadata/schema_VIPS_test_json](/DSS_metadata/schema_VIPS_test.json) 
* For Openalea [openalea_schema.json](/DSS_metadata/openalea_schema.json) 


## Terms definition

### Properties description can be issue from schema

| properties |container| Type | reference | description |
|--|--|--|--|--|
| address | |Text | schema:streetAddress | The street address. For example, 1600 Amphitheatre Pkwy. |
| authors |list| schema:Person | schema:author | The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably. |
| city | |Text | schema:addressLocality | The locality in which the street address is, and which is in the region. For example, Mountain View |
| country | |Text | schema:addressCountry | The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code. |
| description | |Text | schema:description | A description of the item. |
| email | |Text | schema:email | Email address. |
| id | |PropertyValue, URL or Text | schema:identifier | The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See background notes for more details |
| keywords | list|Text | schema:Keywords | Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas. |
| languages |list |Text | schema:availableLanguage | A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard |
| name | |Text | schema:name | schema:Thing | The name of the item.(organisation,model,author) |
| organization | |Text | schema:affiliation | An organization that this person is affiliated with. For example, a school/university, a club, or a team. |
| organization | |schema:Organization | schema:Organization | An organization such as a school, NGO, corporation, club, etc. |
| postal_code | |Text | schema:postalCode | The postal code. For example, 94043. |
| url | |URL | schema:url | schema:Thing | URL of the item. |
| version | |Float | schema:version | The version of the CreativeWork embodied by a specified resource. |
|codeRepository||URL|schema:codeRepository|Link to the repository where the un-compiled, human readable code and related code is located (SVN, GitHub, CodePlex, institutional GitLab instance, etc.|
|programmingLanguage|list|Text|schema:programmingLanguage|The computer programming language.|
|runtimePlatform||Text|schema:runtimePlatform|Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0). Supersedes runtime. |
|downloadUrl||URL|schema:downloadUrl|If the file can be downloaded, URL to download the binary. |
|installUrl||URL|schema:installUrl|URL at which the app may be installed, if different from the URL of the item. |
|operatingSystem|list|Text|schema:operatingSystem|Operating systems supported (Windows 7, OSX 10.6, Android 1.6). |
| citation | list|URL | schema:citation | List of DOI about model |
|contributor|list|schema:Person|schema:contributor|A secondary contributor to the CreativeWork or Event. |
|dateCreated||schema:Date|schema:dateCreated|The date on which the CreativeWork was created or the item was added to a DataFeed. |
|dateModified||schema:Date|schema:dateModified|The date on which the CreativeWork was most recently modified or when the item’s entry was modified within a DataFeed. |
|datePublished||schema:Date|datePublished|Date of first broadcast/publication|
|fileFormat||Text|schema:fileFormat|Media type, typically MIME format (see IANA site) of the content e.g. application/zip of a SoftwareApplication binary. In cases where a CreativeWork has several media type representations, ‘encoding’ can be used to indicate each MediaObject alongside particular fileFormat information. Unregistered or niche file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia entry. |
|funder|list|schema:Organization|schema:funder|A person or organization that supports (sponsors) something through some kind of financial contribution. v|
|licence||schema:URL|schema:licence|A license document that applies to this content, typically indicated by URL.|



### Properties description can be issue from ipmdecision

| properties | container|Type | reference | description |
|--|--|--|--|--|
| DSS_Model | |ipmdecision:DSS_Model | ipmdecision:DSS_Model | model with their descriptions |
| content_type || Text  | ipmdecision:content_type | Regular forms: application/x-www-form-urlencoded , Regular forms with files: multipart/form-data |
| crops |list |Text | ipmdecision:crops | list of crop using EPPO code. See code on <https://gd.eppo.int/> |
| description_URL | |URL | ipmdecision:description_URL | url of documentation about model |
| endpoint | |URL | ipmdecision:endpoint | URL where your service can be accessed by a client application. |
| execution | | | ipmdecision:execution | execution of model |
| form_method | |Text | ipmdecision:form_method | The formmethod attribute specifies which HTTP method to use when sending the form-data,The form-data can be sent as URL variables (with method="get") or as HTTP post (with method="post") definition trouvé dans <https://www.w3schools.com/tags/att_button_formmethod.asp> |
| input_schema | |schema | ipmdecision:input_format | The input template should adhere to the JSON Schema standard: <https://json-schema.org/> |
| interval | |Integer | ipmdecision:interval | Sampling interval in second |
| intput || | ipmdecision:input | datatype input in the model |
| output ||  | ipmdecision:output | Definition of the result parameters specific for this DSS model |
| parameter_code | |integer | ipmdecision:parameter_code | is an identifier for described variable parameter_code id is on <https://github.com/H2020-IPM-Decisions/formats/blob/master/weather_data/> |
| pests | list |Text | ipmdecision:pests | list of a pest using EPPO code See code on <https://gd.eppo.int/> |
| result_parameters ||  | ipmdecision:result_parameters | Definition of the result parameters specific for this DSS model |
| title | |Text|ipmdecision:title|Title of the graph or parameter|
| type_of_decision || Text | ipmdecision:type_of_decision | indicate the type of decision for user |
| type_of_output | |Text | ipmdecision:type_of_output | indicate the type of output |
| valid_spatial | |Text | ipmdecision:valid_spatial (schema:countriesSupported) | spatial validation of model |
| warning_status_interpretation || Text | ipmdecision:warning_status_interpretation | Definition of the warning_station_interpretation specific for this DSS model |
| weather |list | | ipmdecision:weather | weather data for parameter_code is described in <https://github.com/H2020-IPM-Decisions/formats/blob/master/weather_data/weather_parameters_draft_v2.yaml> |

### Properties description can be issue from codemeta

|Properties|container|Type|reference|description|
|--|--|--|--|--|
|maintener|list|schema:Person|codemeta:mainterner|Individual responsible for maintaining the software (usually includes an email contact address)|
|contIntegration||URL|condemeta:contIntegration|link to continuous integration service|
|buildInstruction||URL|codemeta:buildInstruction|link to installation instructions/documentation |
|developmentStatus||URL|codemeta:developmentStatus|Description of development status, e.g. Active, inactive, suspended. See repostatus.org|
|IssueTracker||URL|codemeta:IssueTracker|ink to software bug reporting or issue tracking system|
|readme||URL|codemeta:readme|link to software Readme file|


> **sources:**  
> codemeta-projet: <https://codemeta.github.io/index.html>  
> codemeta terms: <https://codemeta.github.io/terms/>  
> codemeta github: <https://github.com/codemeta/codemeta>

|Warning: Problem with organization first describe organization and in author describe affiliation|
|-|

|Note: It seems that content_type and fileFormat is same things|
|-|


## Questions/remarks
* Wouldn't it be better to identify people also with a unique ex identifier (ORCID number or organigram)? example (https://orcid.org/0000-0001-9923-8817 for M.LABADIE or https://www.nibio.no/en/employees/berit-nordskog for berit NORDSKOG)
* For Pests and Crops EPPO code add url and identifier of the description of EPPO (https://gd.eppo.int/taxon/PSILRO for pest, https://gd.eppo.int/taxon/DAUCS for crops)
* Is there a JSON for weather data that could be linked to the json LD or a table with identifier and description? 
* DateCreated ect is important or not? 


