# update-transformerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/update-transformer.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/update-transformer.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [b2bi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/index.html#cli-aws-b2bi) ]

# update-transformer

## Description

Updates the specified parameters for a transformer. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/b2bi-2022-06-23/UpdateTransformer)

## Synopsis

```
update-transformer
--transformer-id <value>
[--name <value>]
[--status <value>]
[--file-format <value>]
[--mapping-template <value>]
[--edi-type <value>]
[--sample-document <value>]
[--input-conversion <value>]
[--mapping <value>]
[--output-conversion <value>]
[--sample-documents <value>]
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--transformer-id` (string)

Specifies the system-assigned unique identifier for the transformer.

`--name` (string)

Specify a new name for the transformer, if you want to update it.

`--status` (string)

Specifies the transformerâs status. You can update the state of the transformer from `inactive` to `active` .

Possible values:

- `active`
- `inactive`

`--file-format` (string)

Specifies that the currently supported file formats for EDI transformations are `JSON` and `XML` .

Possible values:

- `XML`
- `JSON`
- `NOT_USED`

`--mapping-template` (string)

Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.

### Note

This parameter is available for backwards compatibility. Use the [Mapping](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html) data type instead.

`--edi-type` (tagged union structure)

Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `x12Details`.

x12Details -> (structure)

Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

transactionSet -> (string)

Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.

version -> (string)

Returns the version to use for the specified X12 transaction set.

Shorthand Syntax:

```
x12Details={transactionSet=string,version=string}
```

JSON Syntax:

```
{
  "x12Details": {
    "transactionSet": "X12_100"|"X12_101"|"X12_102"|"X12_103"|"X12_104"|"X12_105"|"X12_106"|"X12_107"|"X12_108"|"X12_109"|"X12_110"|"X12_111"|"X12_112"|"X12_113"|"X12_120"|"X12_121"|"X12_124"|"X12_125"|"X12_126"|"X12_127"|"X12_128"|"X12_129"|"X12_130"|"X12_131"|"X12_132"|"X12_133"|"X12_135"|"X12_138"|"X12_139"|"X12_140"|"X12_141"|"X12_142"|"X12_143"|"X12_144"|"X12_146"|"X12_147"|"X12_148"|"X12_149"|"X12_150"|"X12_151"|"X12_152"|"X12_153"|"X12_154"|"X12_155"|"X12_157"|"X12_158"|"X12_159"|"X12_160"|"X12_161"|"X12_163"|"X12_170"|"X12_175"|"X12_176"|"X12_179"|"X12_180"|"X12_185"|"X12_186"|"X12_187"|"X12_188"|"X12_189"|"X12_190"|"X12_191"|"X12_194"|"X12_195"|"X12_196"|"X12_197"|"X12_198"|"X12_199"|"X12_200"|"X12_201"|"X12_202"|"X12_203"|"X12_204"|"X12_205"|"X12_206"|"X12_210"|"X12_211"|"X12_212"|"X12_213"|"X12_214"|"X12_215"|"X12_216"|"X12_217"|"X12_218"|"X12_219"|"X12_220"|"X12_222"|"X12_223"|"X12_224"|"X12_225"|"X12_227"|"X12_228"|"X12_240"|"X12_242"|"X12_244"|"X12_245"|"X12_248"|"X12_249"|"X12_250"|"X12_251"|"X12_252"|"X12_255"|"X12_256"|"X12_259"|"X12_260"|"X12_261"|"X12_262"|"X12_263"|"X12_264"|"X12_265"|"X12_266"|"X12_267"|"X12_268"|"X12_269"|"X12_270"|"X12_271"|"X12_272"|"X12_273"|"X12_274"|"X12_275"|"X12_276"|"X12_277"|"X12_278"|"X12_280"|"X12_283"|"X12_284"|"X12_285"|"X12_286"|"X12_288"|"X12_290"|"X12_300"|"X12_301"|"X12_303"|"X12_304"|"X12_309"|"X12_310"|"X12_311"|"X12_312"|"X12_313"|"X12_315"|"X12_317"|"X12_319"|"X12_322"|"X12_323"|"X12_324"|"X12_325"|"X12_326"|"X12_350"|"X12_352"|"X12_353"|"X12_354"|"X12_355"|"X12_356"|"X12_357"|"X12_358"|"X12_361"|"X12_362"|"X12_404"|"X12_410"|"X12_412"|"X12_414"|"X12_417"|"X12_418"|"X12_419"|"X12_420"|"X12_421"|"X12_422"|"X12_423"|"X12_424"|"X12_425"|"X12_426"|"X12_429"|"X12_431"|"X12_432"|"X12_433"|"X12_434"|"X12_435"|"X12_436"|"X12_437"|"X12_440"|"X12_451"|"X12_452"|"X12_453"|"X12_455"|"X12_456"|"X12_460"|"X12_463"|"X12_466"|"X12_468"|"X12_470"|"X12_475"|"X12_485"|"X12_486"|"X12_490"|"X12_492"|"X12_494"|"X12_500"|"X12_501"|"X12_503"|"X12_504"|"X12_511"|"X12_517"|"X12_521"|"X12_527"|"X12_536"|"X12_540"|"X12_561"|"X12_567"|"X12_568"|"X12_601"|"X12_602"|"X12_620"|"X12_625"|"X12_650"|"X12_715"|"X12_753"|"X12_754"|"X12_805"|"X12_806"|"X12_810"|"X12_811"|"X12_812"|"X12_813"|"X12_814"|"X12_815"|"X12_816"|"X12_818"|"X12_819"|"X12_820"|"X12_821"|"X12_822"|"X12_823"|"X12_824"|"X12_826"|"X12_827"|"X12_828"|"X12_829"|"X12_830"|"X12_831"|"X12_832"|"X12_833"|"X12_834"|"X12_835"|"X12_836"|"X12_837"|"X12_838"|"X12_839"|"X12_840"|"X12_841"|"X12_842"|"X12_843"|"X12_844"|"X12_845"|"X12_846"|"X12_847"|"X12_848"|"X12_849"|"X12_850"|"X12_851"|"X12_852"|"X12_853"|"X12_854"|"X12_855"|"X12_856"|"X12_857"|"X12_858"|"X12_859"|"X12_860"|"X12_861"|"X12_862"|"X12_863"|"X12_864"|"X12_865"|"X12_866"|"X12_867"|"X12_868"|"X12_869"|"X12_870"|"X12_871"|"X12_872"|"X12_873"|"X12_874"|"X12_875"|"X12_876"|"X12_877"|"X12_878"|"X12_879"|"X12_880"|"X12_881"|"X12_882"|"X12_883"|"X12_884"|"X12_885"|"X12_886"|"X12_887"|"X12_888"|"X12_889"|"X12_891"|"X12_893"|"X12_894"|"X12_895"|"X12_896"|"X12_920"|"X12_924"|"X12_925"|"X12_926"|"X12_928"|"X12_940"|"X12_943"|"X12_944"|"X12_945"|"X12_947"|"X12_980"|"X12_990"|"X12_993"|"X12_996"|"X12_997"|"X12_998"|"X12_999"|"X12_270_X279"|"X12_271_X279"|"X12_275_X210"|"X12_275_X211"|"X12_276_X212"|"X12_277_X212"|"X12_277_X214"|"X12_277_X364"|"X12_278_X217"|"X12_820_X218"|"X12_820_X306"|"X12_824_X186"|"X12_834_X220"|"X12_834_X307"|"X12_834_X318"|"X12_835_X221"|"X12_837_X222"|"X12_837_X223"|"X12_837_X224"|"X12_837_X291"|"X12_837_X292"|"X12_837_X298"|"X12_999_X231",
    "version": "VERSION_4010"|"VERSION_4030"|"VERSION_4050"|"VERSION_4060"|"VERSION_5010"|"VERSION_5010_HIPAA"
  }
}
```

`--sample-document` (string)

Specifies a sample EDI document that is used by a transformer as a guide for processing the EDI data.

`--input-conversion` (structure)

To update, specify the `InputConversion` object, which contains the format options for the inbound transformation.

fromFormat -> (string)

The format for the transformer input: currently on `X12` is supported.

formatOptions -> (tagged union structure)

A structure that contains the formatting options for an inbound transformer.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `x12`.

x12 -> (structure)

A structure that contains the X12 transaction set and version. The X12 structure is used when the system transforms an EDI (electronic data interchange) file.

### Note

If an EDI input file contains more than one transaction, each transaction must have the same transaction set and version, for example 214/4010. If not, the transformer cannot parse the file.

transactionSet -> (string)

Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.

version -> (string)

Returns the version to use for the specified X12 transaction set.

Shorthand Syntax:

```
fromFormat=string,formatOptions={x12={transactionSet=string,version=string}}
```

JSON Syntax:

```
{
  "fromFormat": "X12",
  "formatOptions": {
    "x12": {
      "transactionSet": "X12_100"|"X12_101"|"X12_102"|"X12_103"|"X12_104"|"X12_105"|"X12_106"|"X12_107"|"X12_108"|"X12_109"|"X12_110"|"X12_111"|"X12_112"|"X12_113"|"X12_120"|"X12_121"|"X12_124"|"X12_125"|"X12_126"|"X12_127"|"X12_128"|"X12_129"|"X12_130"|"X12_131"|"X12_132"|"X12_133"|"X12_135"|"X12_138"|"X12_139"|"X12_140"|"X12_141"|"X12_142"|"X12_143"|"X12_144"|"X12_146"|"X12_147"|"X12_148"|"X12_149"|"X12_150"|"X12_151"|"X12_152"|"X12_153"|"X12_154"|"X12_155"|"X12_157"|"X12_158"|"X12_159"|"X12_160"|"X12_161"|"X12_163"|"X12_170"|"X12_175"|"X12_176"|"X12_179"|"X12_180"|"X12_185"|"X12_186"|"X12_187"|"X12_188"|"X12_189"|"X12_190"|"X12_191"|"X12_194"|"X12_195"|"X12_196"|"X12_197"|"X12_198"|"X12_199"|"X12_200"|"X12_201"|"X12_202"|"X12_203"|"X12_204"|"X12_205"|"X12_206"|"X12_210"|"X12_211"|"X12_212"|"X12_213"|"X12_214"|"X12_215"|"X12_216"|"X12_217"|"X12_218"|"X12_219"|"X12_220"|"X12_222"|"X12_223"|"X12_224"|"X12_225"|"X12_227"|"X12_228"|"X12_240"|"X12_242"|"X12_244"|"X12_245"|"X12_248"|"X12_249"|"X12_250"|"X12_251"|"X12_252"|"X12_255"|"X12_256"|"X12_259"|"X12_260"|"X12_261"|"X12_262"|"X12_263"|"X12_264"|"X12_265"|"X12_266"|"X12_267"|"X12_268"|"X12_269"|"X12_270"|"X12_271"|"X12_272"|"X12_273"|"X12_274"|"X12_275"|"X12_276"|"X12_277"|"X12_278"|"X12_280"|"X12_283"|"X12_284"|"X12_285"|"X12_286"|"X12_288"|"X12_290"|"X12_300"|"X12_301"|"X12_303"|"X12_304"|"X12_309"|"X12_310"|"X12_311"|"X12_312"|"X12_313"|"X12_315"|"X12_317"|"X12_319"|"X12_322"|"X12_323"|"X12_324"|"X12_325"|"X12_326"|"X12_350"|"X12_352"|"X12_353"|"X12_354"|"X12_355"|"X12_356"|"X12_357"|"X12_358"|"X12_361"|"X12_362"|"X12_404"|"X12_410"|"X12_412"|"X12_414"|"X12_417"|"X12_418"|"X12_419"|"X12_420"|"X12_421"|"X12_422"|"X12_423"|"X12_424"|"X12_425"|"X12_426"|"X12_429"|"X12_431"|"X12_432"|"X12_433"|"X12_434"|"X12_435"|"X12_436"|"X12_437"|"X12_440"|"X12_451"|"X12_452"|"X12_453"|"X12_455"|"X12_456"|"X12_460"|"X12_463"|"X12_466"|"X12_468"|"X12_470"|"X12_475"|"X12_485"|"X12_486"|"X12_490"|"X12_492"|"X12_494"|"X12_500"|"X12_501"|"X12_503"|"X12_504"|"X12_511"|"X12_517"|"X12_521"|"X12_527"|"X12_536"|"X12_540"|"X12_561"|"X12_567"|"X12_568"|"X12_601"|"X12_602"|"X12_620"|"X12_625"|"X12_650"|"X12_715"|"X12_753"|"X12_754"|"X12_805"|"X12_806"|"X12_810"|"X12_811"|"X12_812"|"X12_813"|"X12_814"|"X12_815"|"X12_816"|"X12_818"|"X12_819"|"X12_820"|"X12_821"|"X12_822"|"X12_823"|"X12_824"|"X12_826"|"X12_827"|"X12_828"|"X12_829"|"X12_830"|"X12_831"|"X12_832"|"X12_833"|"X12_834"|"X12_835"|"X12_836"|"X12_837"|"X12_838"|"X12_839"|"X12_840"|"X12_841"|"X12_842"|"X12_843"|"X12_844"|"X12_845"|"X12_846"|"X12_847"|"X12_848"|"X12_849"|"X12_850"|"X12_851"|"X12_852"|"X12_853"|"X12_854"|"X12_855"|"X12_856"|"X12_857"|"X12_858"|"X12_859"|"X12_860"|"X12_861"|"X12_862"|"X12_863"|"X12_864"|"X12_865"|"X12_866"|"X12_867"|"X12_868"|"X12_869"|"X12_870"|"X12_871"|"X12_872"|"X12_873"|"X12_874"|"X12_875"|"X12_876"|"X12_877"|"X12_878"|"X12_879"|"X12_880"|"X12_881"|"X12_882"|"X12_883"|"X12_884"|"X12_885"|"X12_886"|"X12_887"|"X12_888"|"X12_889"|"X12_891"|"X12_893"|"X12_894"|"X12_895"|"X12_896"|"X12_920"|"X12_924"|"X12_925"|"X12_926"|"X12_928"|"X12_940"|"X12_943"|"X12_944"|"X12_945"|"X12_947"|"X12_980"|"X12_990"|"X12_993"|"X12_996"|"X12_997"|"X12_998"|"X12_999"|"X12_270_X279"|"X12_271_X279"|"X12_275_X210"|"X12_275_X211"|"X12_276_X212"|"X12_277_X212"|"X12_277_X214"|"X12_277_X364"|"X12_278_X217"|"X12_820_X218"|"X12_820_X306"|"X12_824_X186"|"X12_834_X220"|"X12_834_X307"|"X12_834_X318"|"X12_835_X221"|"X12_837_X222"|"X12_837_X223"|"X12_837_X224"|"X12_837_X291"|"X12_837_X292"|"X12_837_X298"|"X12_999_X231",
      "version": "VERSION_4010"|"VERSION_4030"|"VERSION_4050"|"VERSION_4060"|"VERSION_5010"|"VERSION_5010_HIPAA"
    }
  }
}
```

`--mapping` (structure)

Specify the structure that contains the mapping template and its language (either XSLT or JSONATA).

templateLanguage -> (string)

The transformation language for the template, either XSLT or JSONATA.

template -> (string)

A string that represents the mapping template, in the transformation language specified in `templateLanguage` .

Shorthand Syntax:

```
templateLanguage=string,template=string
```

JSON Syntax:

```
{
  "templateLanguage": "XSLT"|"JSONATA",
  "template": "string"
}
```

`--output-conversion` (structure)

To update, specify the `OutputConversion` object, which contains the format options for the outbound transformation.

toFormat -> (string)

The format for the output from an outbound transformer: only X12 is currently supported.

formatOptions -> (tagged union structure)

A structure that contains the X12 transaction set and version for the transformer output.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `x12`.

x12 -> (structure)

A structure that contains the X12 transaction set and version. The X12 structure is used when the system transforms an EDI (electronic data interchange) file.

### Note

If an EDI input file contains more than one transaction, each transaction must have the same transaction set and version, for example 214/4010. If not, the transformer cannot parse the file.

transactionSet -> (string)

Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.

version -> (string)

Returns the version to use for the specified X12 transaction set.

Shorthand Syntax:

```
toFormat=string,formatOptions={x12={transactionSet=string,version=string}}
```

JSON Syntax:

```
{
  "toFormat": "X12",
  "formatOptions": {
    "x12": {
      "transactionSet": "X12_100"|"X12_101"|"X12_102"|"X12_103"|"X12_104"|"X12_105"|"X12_106"|"X12_107"|"X12_108"|"X12_109"|"X12_110"|"X12_111"|"X12_112"|"X12_113"|"X12_120"|"X12_121"|"X12_124"|"X12_125"|"X12_126"|"X12_127"|"X12_128"|"X12_129"|"X12_130"|"X12_131"|"X12_132"|"X12_133"|"X12_135"|"X12_138"|"X12_139"|"X12_140"|"X12_141"|"X12_142"|"X12_143"|"X12_144"|"X12_146"|"X12_147"|"X12_148"|"X12_149"|"X12_150"|"X12_151"|"X12_152"|"X12_153"|"X12_154"|"X12_155"|"X12_157"|"X12_158"|"X12_159"|"X12_160"|"X12_161"|"X12_163"|"X12_170"|"X12_175"|"X12_176"|"X12_179"|"X12_180"|"X12_185"|"X12_186"|"X12_187"|"X12_188"|"X12_189"|"X12_190"|"X12_191"|"X12_194"|"X12_195"|"X12_196"|"X12_197"|"X12_198"|"X12_199"|"X12_200"|"X12_201"|"X12_202"|"X12_203"|"X12_204"|"X12_205"|"X12_206"|"X12_210"|"X12_211"|"X12_212"|"X12_213"|"X12_214"|"X12_215"|"X12_216"|"X12_217"|"X12_218"|"X12_219"|"X12_220"|"X12_222"|"X12_223"|"X12_224"|"X12_225"|"X12_227"|"X12_228"|"X12_240"|"X12_242"|"X12_244"|"X12_245"|"X12_248"|"X12_249"|"X12_250"|"X12_251"|"X12_252"|"X12_255"|"X12_256"|"X12_259"|"X12_260"|"X12_261"|"X12_262"|"X12_263"|"X12_264"|"X12_265"|"X12_266"|"X12_267"|"X12_268"|"X12_269"|"X12_270"|"X12_271"|"X12_272"|"X12_273"|"X12_274"|"X12_275"|"X12_276"|"X12_277"|"X12_278"|"X12_280"|"X12_283"|"X12_284"|"X12_285"|"X12_286"|"X12_288"|"X12_290"|"X12_300"|"X12_301"|"X12_303"|"X12_304"|"X12_309"|"X12_310"|"X12_311"|"X12_312"|"X12_313"|"X12_315"|"X12_317"|"X12_319"|"X12_322"|"X12_323"|"X12_324"|"X12_325"|"X12_326"|"X12_350"|"X12_352"|"X12_353"|"X12_354"|"X12_355"|"X12_356"|"X12_357"|"X12_358"|"X12_361"|"X12_362"|"X12_404"|"X12_410"|"X12_412"|"X12_414"|"X12_417"|"X12_418"|"X12_419"|"X12_420"|"X12_421"|"X12_422"|"X12_423"|"X12_424"|"X12_425"|"X12_426"|"X12_429"|"X12_431"|"X12_432"|"X12_433"|"X12_434"|"X12_435"|"X12_436"|"X12_437"|"X12_440"|"X12_451"|"X12_452"|"X12_453"|"X12_455"|"X12_456"|"X12_460"|"X12_463"|"X12_466"|"X12_468"|"X12_470"|"X12_475"|"X12_485"|"X12_486"|"X12_490"|"X12_492"|"X12_494"|"X12_500"|"X12_501"|"X12_503"|"X12_504"|"X12_511"|"X12_517"|"X12_521"|"X12_527"|"X12_536"|"X12_540"|"X12_561"|"X12_567"|"X12_568"|"X12_601"|"X12_602"|"X12_620"|"X12_625"|"X12_650"|"X12_715"|"X12_753"|"X12_754"|"X12_805"|"X12_806"|"X12_810"|"X12_811"|"X12_812"|"X12_813"|"X12_814"|"X12_815"|"X12_816"|"X12_818"|"X12_819"|"X12_820"|"X12_821"|"X12_822"|"X12_823"|"X12_824"|"X12_826"|"X12_827"|"X12_828"|"X12_829"|"X12_830"|"X12_831"|"X12_832"|"X12_833"|"X12_834"|"X12_835"|"X12_836"|"X12_837"|"X12_838"|"X12_839"|"X12_840"|"X12_841"|"X12_842"|"X12_843"|"X12_844"|"X12_845"|"X12_846"|"X12_847"|"X12_848"|"X12_849"|"X12_850"|"X12_851"|"X12_852"|"X12_853"|"X12_854"|"X12_855"|"X12_856"|"X12_857"|"X12_858"|"X12_859"|"X12_860"|"X12_861"|"X12_862"|"X12_863"|"X12_864"|"X12_865"|"X12_866"|"X12_867"|"X12_868"|"X12_869"|"X12_870"|"X12_871"|"X12_872"|"X12_873"|"X12_874"|"X12_875"|"X12_876"|"X12_877"|"X12_878"|"X12_879"|"X12_880"|"X12_881"|"X12_882"|"X12_883"|"X12_884"|"X12_885"|"X12_886"|"X12_887"|"X12_888"|"X12_889"|"X12_891"|"X12_893"|"X12_894"|"X12_895"|"X12_896"|"X12_920"|"X12_924"|"X12_925"|"X12_926"|"X12_928"|"X12_940"|"X12_943"|"X12_944"|"X12_945"|"X12_947"|"X12_980"|"X12_990"|"X12_993"|"X12_996"|"X12_997"|"X12_998"|"X12_999"|"X12_270_X279"|"X12_271_X279"|"X12_275_X210"|"X12_275_X211"|"X12_276_X212"|"X12_277_X212"|"X12_277_X214"|"X12_277_X364"|"X12_278_X217"|"X12_820_X218"|"X12_820_X306"|"X12_824_X186"|"X12_834_X220"|"X12_834_X307"|"X12_834_X318"|"X12_835_X221"|"X12_837_X222"|"X12_837_X223"|"X12_837_X224"|"X12_837_X291"|"X12_837_X292"|"X12_837_X298"|"X12_999_X231",
      "version": "VERSION_4010"|"VERSION_4030"|"VERSION_4050"|"VERSION_4060"|"VERSION_5010"|"VERSION_5010_HIPAA"
    }
  }
}
```

`--sample-documents` (structure)

Specify a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.

bucketName -> (string)

Contains the Amazon S3 bucket that is used to hold your sample documents.

keys -> (list)

Contains an array of the Amazon S3 keys used to identify the location for your sample documents.

(structure)

An array of the Amazon S3 keys used to identify the location for your sample documents.

input -> (string)

An array of keys for your input sample documents.

output -> (string)

An array of keys for your output sample documents.

Shorthand Syntax:

```
bucketName=string,keys=[{input=string,output=string},{input=string,output=string}]
```

JSON Syntax:

```
{
  "bucketName": "string",
  "keys": [
    {
      "input": "string",
      "output": "string"
    }
    ...
  ]
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Output

transformerId -> (string)

Returns the system-assigned unique identifier for the transformer.

transformerArn -> (string)

Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.

name -> (string)

Returns the name of the transformer.

status -> (string)

Returns the state of the newly created transformer. The transformer can be either `active` or `inactive` . For the transformer to be used in a capability, its status must `active` .

createdAt -> (timestamp)

Returns a timestamp for creation date and time of the transformer.

modifiedAt -> (timestamp)

Returns a timestamp for last time the transformer was modified.

fileFormat -> (string)

Returns that the currently supported file formats for EDI transformations are `JSON` and `XML` .

mappingTemplate -> (string)

Returns the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.

ediType -> (tagged union structure)

Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `x12Details`.

x12Details -> (structure)

Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

transactionSet -> (string)

Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.

version -> (string)

Returns the version to use for the specified X12 transaction set.

sampleDocument -> (string)

Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.

inputConversion -> (structure)

Returns the `InputConversion` object, which contains the format options for the inbound transformation.

fromFormat -> (string)

The format for the transformer input: currently on `X12` is supported.

formatOptions -> (tagged union structure)

A structure that contains the formatting options for an inbound transformer.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `x12`.

x12 -> (structure)

A structure that contains the X12 transaction set and version. The X12 structure is used when the system transforms an EDI (electronic data interchange) file.

### Note

If an EDI input file contains more than one transaction, each transaction must have the same transaction set and version, for example 214/4010. If not, the transformer cannot parse the file.

transactionSet -> (string)

Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.

version -> (string)

Returns the version to use for the specified X12 transaction set.

mapping -> (structure)

Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).

templateLanguage -> (string)

The transformation language for the template, either XSLT or JSONATA.

template -> (string)

A string that represents the mapping template, in the transformation language specified in `templateLanguage` .

outputConversion -> (structure)

Returns the `OutputConversion` object, which contains the format options for the outbound transformation.

toFormat -> (string)

The format for the output from an outbound transformer: only X12 is currently supported.

formatOptions -> (tagged union structure)

A structure that contains the X12 transaction set and version for the transformer output.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `x12`.

x12 -> (structure)

A structure that contains the X12 transaction set and version. The X12 structure is used when the system transforms an EDI (electronic data interchange) file.

### Note

If an EDI input file contains more than one transaction, each transaction must have the same transaction set and version, for example 214/4010. If not, the transformer cannot parse the file.

transactionSet -> (string)

Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.

version -> (string)

Returns the version to use for the specified X12 transaction set.

sampleDocuments -> (structure)

Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.

bucketName -> (string)

Contains the Amazon S3 bucket that is used to hold your sample documents.

keys -> (list)

Contains an array of the Amazon S3 keys used to identify the location for your sample documents.

(structure)

An array of the Amazon S3 keys used to identify the location for your sample documents.

input -> (string)

An array of keys for your input sample documents.

output -> (string)

An array of keys for your output sample documents.