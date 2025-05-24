# lambdaÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# lambda

## Description

**Overview**

Lambda is a compute service that lets you run code without provisioning or managing servers. Lambda runs your code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, code monitoring and logging. With Lambda, you can run code for virtually any type of application or backend service. For more information about the Lambda service, see [What is Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) in the **Lambda Developer Guide** .

The *Lambda API Reference* provides information about each of the API methods, including details about the parameters in each API request and response.

You can use Software Development Kits (SDKs), Integrated Development Environment (IDE) Toolkits, and command line tools to access the API. For installation instructions, see [Tools for Amazon Web Services](http://aws.amazon.com/tools/) .

For a list of Region-specific endpoints that Lambda supports, see [Lambda endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/lambda-service.html) in the *Amazon Web Services General Reference.* .

When making the API calls, you will need to authenticate your request by providing a signature. Lambda supports signature version 4. For more information, see [Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon Web Services General Reference.* .

**CA certificates**

Because Amazon Web Services SDKs use the CA certificates from your computer, changes to the certificates on the Amazon Web Services servers can cause connection failures when you attempt to use an SDK. You can prevent these failures by keeping your computerâs CA certificates and operating system up-to-date. If you encounter this issue in a corporate environment and do not manage your own computer, you might need to ask an administrator to assist with the update process. The following list shows minimum operating system and Java versions:

- Microsoft Windows versions that have updates from January 2005 or later installed contain at least one of the required CAs in their trust list.
- Mac OS X 10.4 with Java for Mac OS X 10.4 Release 5 (February 2007), Mac OS X 10.5 (October 2007), and later versions contain at least one of the required CAs in their trust list.
- Red Hat Enterprise Linux 5 (March 2007), 6, and 7 and CentOS 5, 6, and 7 all contain at least one of the required CAs in their default trusted CA list.
- Java 1.4.2_12 (May 2006), 5 Update 2 (March 2005), and all later versions, including Java 6 (December 2006), 7, and 8, contain at least one of the required CAs in their default trusted CA list.

When accessing the Lambda management console or Lambda API endpoints, whether through browsers or programmatically, you will need to ensure your client machines support any of the following CAs:

- Amazon Root CA 1
- Starfield Services Root Certificate Authority - G2
- Starfield Class 2 Certification Authority

Root certificates from the first two authorities are available from [Amazon trust services](https://www.amazontrust.com/repository/) , but keeping your computer up-to-date is the more straightforward solution. To learn more about ACM-provided certificates, see [Amazon Web Services Certificate Manager FAQs.](http://aws.amazon.com/certificate-manager/faqs/#certificates)

## Available Commands

- [add-layer-version-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-layer-version-permission.html)
- [add-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-permission.html)
- [create-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-alias.html)
- [create-code-signing-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-code-signing-config.html)
- [create-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html)
- [create-function](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html)
- [create-function-url-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function-url-config.html)
- [delete-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-alias.html)
- [delete-code-signing-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-code-signing-config.html)
- [delete-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-event-source-mapping.html)
- [delete-function](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function.html)
- [delete-function-code-signing-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-code-signing-config.html)
- [delete-function-concurrency](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-concurrency.html)
- [delete-function-event-invoke-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-event-invoke-config.html)
- [delete-function-url-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-url-config.html)
- [delete-layer-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-layer-version.html)
- [delete-provisioned-concurrency-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-provisioned-concurrency-config.html)
- [get-account-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-account-settings.html)
- [get-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-alias.html)
- [get-code-signing-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-code-signing-config.html)
- [get-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-event-source-mapping.html)
- [get-function](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function.html)
- [get-function-code-signing-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-code-signing-config.html)
- [get-function-concurrency](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-concurrency.html)
- [get-function-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-configuration.html)
- [get-function-event-invoke-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-event-invoke-config.html)
- [get-function-recursion-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-recursion-config.html)
- [get-function-url-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-url-config.html)
- [get-layer-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version.html)
- [get-layer-version-by-arn](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version-by-arn.html)
- [get-layer-version-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version-policy.html)
- [get-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-policy.html)
- [get-provisioned-concurrency-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-provisioned-concurrency-config.html)
- [get-runtime-management-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-runtime-management-config.html)
- [invoke](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html)
- [list-aliases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-aliases.html)
- [list-code-signing-configs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-code-signing-configs.html)
- [list-event-source-mappings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-event-source-mappings.html)
- [list-function-event-invoke-configs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-function-event-invoke-configs.html)
- [list-function-url-configs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-function-url-configs.html)
- [list-functions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-functions.html)
- [list-functions-by-code-signing-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-functions-by-code-signing-config.html)
- [list-layer-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-layer-versions.html)
- [list-layers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-layers.html)
- [list-provisioned-concurrency-configs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-provisioned-concurrency-configs.html)
- [list-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-tags.html)
- [list-versions-by-function](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-versions-by-function.html)
- [publish-layer-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html)
- [publish-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-version.html)
- [put-function-code-signing-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-code-signing-config.html)
- [put-function-concurrency](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-concurrency.html)
- [put-function-event-invoke-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-event-invoke-config.html)
- [put-function-recursion-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-recursion-config.html)
- [put-provisioned-concurrency-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-provisioned-concurrency-config.html)
- [put-runtime-management-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-runtime-management-config.html)
- [remove-layer-version-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/remove-layer-version-permission.html)
- [remove-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/remove-permission.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/untag-resource.html)
- [update-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-alias.html)
- [update-code-signing-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-code-signing-config.html)
- [update-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html)
- [update-function-code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html)
- [update-function-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html)
- [update-function-event-invoke-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-event-invoke-config.html)
- [update-function-url-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-url-config.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/wait/index.html)
- [wizard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/wizard/index.html)