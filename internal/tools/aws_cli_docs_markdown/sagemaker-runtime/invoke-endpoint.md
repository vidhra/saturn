# invoke-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-runtime/invoke-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-runtime/invoke-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-runtime/index.html#cli-aws-sagemaker-runtime) ]

# invoke-endpoint

## Description

After you deploy a model into production using Amazon SageMaker hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint.

For an overview of Amazon SageMaker, see [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html) .

Amazon SageMaker strips all POST headers except those supported by the API. Amazon SageMaker might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax.

Calls to `InvokeEndpoint` are authenticated by using Amazon Web Services Signature Version 4. For information, see [Authenticating Requests (Amazon Web Services Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) in the *Amazon S3 API Reference* .

A customerâs model containers must respond to requests within 60 seconds. The model itself can have a maximum processing time of 60 seconds before responding to invocations. If your model is going to take 50-60 seconds of processing time, the SDK socket timeout should be set to be 70 seconds.

### Note

Endpoints are scoped to an individual account, and are not public. The URL does not contain the account ID, but Amazon SageMaker determines the account ID from the authentication token that is supplied by the caller.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/runtime.sagemaker-2017-05-13/InvokeEndpoint)

## Synopsis

```
invoke-endpoint
--endpoint-name <value>
--body <value>
[--content-type <value>]
[--accept <value>]
[--custom-attributes <value>]
[--target-model <value>]
[--target-variant <value>]
[--target-container-hostname <value>]
[--inference-id <value>]
[--enable-explanations <value>]
[--inference-component-name <value>]
[--session-id <value>]
<outfile>
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

`--endpoint-name` (string)

The name of the endpoint that you specified when you created the endpoint using the [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html) API.

`--body` (blob)

Provides input data, in the format specified in the `ContentType` request header. Amazon SageMaker passes all of the data in the body to the model.

For information about the format of the request body, see [Common Data Formats-Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html) .

`--content-type` (string)

The MIME type of the input data in the request body.

`--accept` (string)

The desired MIME type of the inference response from the model container.

`--custom-attributes` (string)

Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in [Section 3.3.6. Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6) of the Hypertext Transfer Protocol (HTTP/1.1).

The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with `Trace ID:` in your post-processing function.

This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker Python SDK.

`--target-model` (string)

The model to request for inference when invoking a multi-model endpoint.

`--target-variant` (string)

Specify the production variant to send the inference request to when invoking an endpoint that is running two or more variants. Note that this parameter overrides the default behavior for the endpoint, which is to distribute the invocation traffic based on the variant weights.

For information about how to use variant targeting to perform a/b testing, see [Test models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html)

`--target-container-hostname` (string)

If the endpoint hosts multiple containers and is configured to use direct invocation, this parameter specifies the host name of the container to invoke.

`--inference-id` (string)

If you provide a value, it is added to the captured data when you enable data capture on the endpoint. For information about data capture, see [Capture Data](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html) .

`--enable-explanations` (string)

An optional JMESPath expression used to override the `EnableExplanations` parameter of the `ClarifyExplainerConfig` API. See the [EnableExplanations](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-enable) section in the developer guide for more information.

`--inference-component-name` (string)

If the endpoint hosts one or more inference components, this parameter specifies the name of inference component to invoke.

`--session-id` (string)

Creates a stateful session or identifies an existing one. You can do one of the following:

- Create a stateful session by specifying the value `NEW_SESSION` .
- Send your request to an existing stateful session by specifying the ID of that session.

With a stateful session, you can send multiple requests to a stateful model. When you create a session with a stateful model, the model must create the session ID and set the expiration time. The model must also provide that information in the response to your request. You can get the ID and timestamp from the `NewSessionId` response parameter. For any subsequent request where you specify that session ID, SageMaker routes the request to the same instance that supports the session.

`outfile` (string)
Filename where the content will be saved

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

Body -> (blob)

Includes the inference provided by the model.

For information about the format of the response body, see [Common Data Formats-Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html) .

If the explainer is activated, the body includes the explanations provided by the model. For more information, see the **Response section** under [Invoke the Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response) in the Developer Guide.

ContentType -> (string)

The MIME type of the inference returned from the model container.

InvokedProductionVariant -> (string)

Identifies the production variant that was invoked.

CustomAttributes -> (string)

Provides additional information in the response about the inference returned by a model hosted at an Amazon SageMaker endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to return an ID received in the `CustomAttributes` header of a request or other metadata that a service endpoint was programmed to produce. The value must consist of no more than 1024 visible US-ASCII characters as specified in [Section 3.3.6. Field Value Components](https://tools.ietf.org/html/rfc7230#section-3.2.6) of the Hypertext Transfer Protocol (HTTP/1.1). If the customer wants the custom attribute returned, the model must set the custom attribute to be included on the way back.

The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with `Trace ID:` in your post-processing function.

This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker Python SDK.

NewSessionId -> (string)

If you created a stateful session with your request, the ID and expiration time that the model assigns to that session.

ClosedSessionId -> (string)

If you closed a stateful session with your request, the ID of that session.