# iot-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# iot-data

## Description

IoT data enables secure, bi-directional communication between Internet-connected things (such as sensors, actuators, embedded devices, or smart appliances) and the Amazon Web Services cloud. It implements a broker for applications and things to publish messages over HTTP (Publish) and retrieve, update, and delete shadows. A shadow is a persistent representation of your things and their state in the Amazon Web Services cloud.

Find the endpoint address for actions in IoT data by running this CLI command:

`aws iot describe-endpoint --endpoint-type iot:Data-ATS`

The service name used by [Amazon Web ServicesSignature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to sign requests is: *iotdevicegateway* .

### Note

For production code it is strongly recommended to use the custom endpoint for your account (retrievable via the iot describe-endpoint command) to ensure best availability and reachability of the service. The default endpoints (intended for testing purposes only) can be found at [https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-data-plane-endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-data-plane-endpoints)

## Available Commands

- [delete-thing-shadow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/delete-thing-shadow.html)
- [get-retained-message](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/get-retained-message.html)
- [get-thing-shadow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/get-thing-shadow.html)
- [list-named-shadows-for-thing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/list-named-shadows-for-thing.html)
- [list-retained-messages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/list-retained-messages.html)
- [publish](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/publish.html)
- [update-thing-shadow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/update-thing-shadow.html)