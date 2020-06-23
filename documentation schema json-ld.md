# Documentation of Json-LD

**source:**

* <https://codemeta.github.io/terms/>
* <https://codemeta.github.io/crosswalk/github/>
* <https://codemeta.github.io/crosswalk/python/>
* <http://schema.org/>

# Correspondence table of fields, membership, their descriptions and cross-referencing

| properties | schema.org | codemeta | Type | description |
|--|--|--|--|--|
|Organization | Organization |  | Organization | An organization such as a school, NGO, corporation, club, etc |
|Person | Person |  | Person | A person (alive, dead, undead, or fictional). |
|affiliation|affiliation||Organization, Person, Text|An organization that this person is affiliated with. For example, a school/university, a club, or a team.|
|applicationCategory|applicationCategory||Text or URL|Type of software application, e.g. 'Game, Multimedia'.|
|author|author||Organization or Person|The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.|
|buildInstructions||buildInstructions|URL|link to installation instructions/documentation|
|citation|citation||CreativeWork, Text|A citation or reference to another creative work, such as another publication, web page, scholarly article, etc|
|codeRepository|codeRepository||URL|Link to the repository where the un-compiled, human readable code and related code is located (SVN, GitHub, CodePlex, institutional GitLab instance, etc.)|
|contIntegration||contIntegration|URL|link to continuous integration service|
|countriesNotSupported|countriesNotSupported||softwareApplication, Text|Countries for which the application is not supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.|
|dateCreated|dateCreated||Date or DateTime|The date on which the CreativeWork was created or the item was added to a DataFeed.|
|dateModified|dateModified||Date or DateTime|The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.|
|description|description||Text|A description of the item.|
|developmentStatus||developmentStatus|Text|Description of development status, e.g. Active, inactive, suspended. See repostatus.org|
|downloadUrl|downloadUrl||URL|If the file can be downloaded, URL to download the binary.|
|email|email||ContactPoint, Organization, Person, Text|Email address.|
|embargoDate||embargoDate|Date|Software may be embargoed from public access until a specified date (e.g. pending publication, 1 year from publication)|
|funding||funding|Text|Funding source (e.g. specific grant)|
| identifier | identifier |  |PropertyValue, Text or URL  | The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. |
|identifier|identifier||URL|URL identifier, ideally an ORCID ID for individuals, a FundRef ID for funders|
|installUrl|installUrl||SoftwareApplication, URL|URL at which the app may be installed, if different from the URL of the item.|
|issueTracker||issueTracker|URL|link to software bug reporting or issue tracking system|
|keywords|keywords||Text|Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.|
|knowsLanguage|knowsLanguage||Language,Text|Of a Person, and less typically of an Organization, to indicate a known language. We do not distinguish skill levels or reading/writing/speaking/signing here. Use language codes from the IETF BCP 47 standard.|
|license|license||CreativeWork or URL|A license document that applies to this content, typically indicated by URL.|
|maintainer|maintainer||Organization or Person|A maintainer of a Dataset, software package (SoftwareApplication), or other Project. A maintainer is a Person or Organization that manages contributions to, and/or publication of, some (typically complex) artifact. It is common for distributions of software and data to be based on "upstream" sources. When maintainer is applied to a specific version of something e.g. a particular version or packaging of a Dataset, it is always possible that the upstream source has a different maintainer.|
|name|name||Text|The name of the item.|
|operatingSystem|operatingSystem||Text|Operating systems supported (Windows 7, OSX 10.6, Android 1.6).|
|programmingLanguage|programmingLanguage||ComputerLanguage or Text|The computer programming language.|
|readme||readme||URL|link to software Readme file|
|referencePublication||referencePublication|ScholarlyArticle|An academic publication related to the software.|
|releaseNotes|releaseNotes||SoftwareApplication,Text or URL|Description of what changed in this version.|
|runtimePlatform|runtimePlatform||SoftwareSourceCode, Text|Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0).|
|softwareApplication|softwareApplication||softwareApplication|A software application.|
|softwareHelp|softwareHelp||SoftwareApplication,CreativeWork|Software application help.|
|softwareRequirements|softwareRequirements|||Text or URL|Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (Examples: DirectX, Java or .NET runtime).|
|softwareSuggestions||softwareSuggestions|SoftwareSourceCode|Optional dependencies , e.g. for optional features, code development, etc.|
|version|version||Number or Text|The version of the CreativeWork embodied by a specified resource.|

>[!NOTE] Problem with identifier two description

>[!WARNING] Input and output formalism.