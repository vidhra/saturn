# iotwirelessÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# iotwireless

## Description

AWS IoT Wireless provides bi-directional communication between internet-connected wireless devices and the AWS Cloud. To onboard both LoRaWAN and Sidewalk devices to AWS IoT, use the IoT Wireless API. These wireless devices use the Low Power Wide Area Networking (LPWAN) communication protocol to communicate with AWS IoT.

Using the API, you can perform create, read, update, and delete operations for your wireless devices, gateways, destinations, and profiles. After onboarding your devices, you can use the API operations to set log levels and monitor your devices with CloudWatch.

You can also use the API operations to create multicast groups and schedule a multicast session for sending a downlink message to devices in the group. By using Firmware Updates Over-The-Air (FUOTA) API operations, you can create a FUOTA task and schedule a session to update the firmware of individual devices or an entire group of devices in a multicast group.

To connect to the AWS IoT Wireless Service, use the Service endpoints as described in [IoT Wireless Service endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-lorawan.html#iot-wireless_region) . You can use both IPv4 and IPv6 protocols to connect to the endpoints and send requests to the AWS IoT Wireless service. For more information, see [Using IPv6 with AWS IoT Wireless](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/wireless-ipv6-access.html) .

## Available Commands

- [associate-aws-account-with-partner-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/associate-aws-account-with-partner-account.html)
- [associate-multicast-group-with-fuota-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/associate-multicast-group-with-fuota-task.html)
- [associate-wireless-device-with-fuota-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/associate-wireless-device-with-fuota-task.html)
- [associate-wireless-device-with-multicast-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/associate-wireless-device-with-multicast-group.html)
- [associate-wireless-device-with-thing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/associate-wireless-device-with-thing.html)
- [associate-wireless-gateway-with-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/associate-wireless-gateway-with-certificate.html)
- [associate-wireless-gateway-with-thing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/associate-wireless-gateway-with-thing.html)
- [cancel-multicast-group-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/cancel-multicast-group-session.html)
- [create-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-destination.html)
- [create-device-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-device-profile.html)
- [create-fuota-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-fuota-task.html)
- [create-multicast-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-multicast-group.html)
- [create-network-analyzer-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-network-analyzer-configuration.html)
- [create-service-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-service-profile.html)
- [create-wireless-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-device.html)
- [create-wireless-gateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-gateway.html)
- [create-wireless-gateway-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-gateway-task.html)
- [create-wireless-gateway-task-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-gateway-task-definition.html)
- [delete-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-destination.html)
- [delete-device-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-device-profile.html)
- [delete-fuota-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-fuota-task.html)
- [delete-multicast-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-multicast-group.html)
- [delete-network-analyzer-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-network-analyzer-configuration.html)
- [delete-queued-messages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-queued-messages.html)
- [delete-service-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-service-profile.html)
- [delete-wireless-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-wireless-device.html)
- [delete-wireless-device-import-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-wireless-device-import-task.html)
- [delete-wireless-gateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-wireless-gateway.html)
- [delete-wireless-gateway-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-wireless-gateway-task.html)
- [delete-wireless-gateway-task-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-wireless-gateway-task-definition.html)
- [deregister-wireless-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/deregister-wireless-device.html)
- [disassociate-aws-account-from-partner-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/disassociate-aws-account-from-partner-account.html)
- [disassociate-multicast-group-from-fuota-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/disassociate-multicast-group-from-fuota-task.html)
- [disassociate-wireless-device-from-fuota-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/disassociate-wireless-device-from-fuota-task.html)
- [disassociate-wireless-device-from-multicast-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/disassociate-wireless-device-from-multicast-group.html)
- [disassociate-wireless-device-from-thing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/disassociate-wireless-device-from-thing.html)
- [disassociate-wireless-gateway-from-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/disassociate-wireless-gateway-from-certificate.html)
- [disassociate-wireless-gateway-from-thing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/disassociate-wireless-gateway-from-thing.html)
- [get-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-destination.html)
- [get-device-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-device-profile.html)
- [get-event-configuration-by-resource-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-event-configuration-by-resource-types.html)
- [get-fuota-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-fuota-task.html)
- [get-log-levels-by-resource-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-log-levels-by-resource-types.html)
- [get-metric-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-metric-configuration.html)
- [get-metrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-metrics.html)
- [get-multicast-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-multicast-group.html)
- [get-multicast-group-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-multicast-group-session.html)
- [get-network-analyzer-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-network-analyzer-configuration.html)
- [get-partner-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-partner-account.html)
- [get-position-estimate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-position-estimate.html)
- [get-resource-event-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-resource-event-configuration.html)
- [get-resource-log-level](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-resource-log-level.html)
- [get-resource-position](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-resource-position.html)
- [get-service-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-service-endpoint.html)
- [get-service-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-service-profile.html)
- [get-wireless-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-device.html)
- [get-wireless-device-import-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-device-import-task.html)
- [get-wireless-device-statistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-device-statistics.html)
- [get-wireless-gateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway.html)
- [get-wireless-gateway-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway-certificate.html)
- [get-wireless-gateway-firmware-information](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway-firmware-information.html)
- [get-wireless-gateway-statistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway-statistics.html)
- [get-wireless-gateway-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway-task.html)
- [get-wireless-gateway-task-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway-task-definition.html)
- [list-destinations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-destinations.html)
- [list-device-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-device-profiles.html)
- [list-devices-for-wireless-device-import-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-devices-for-wireless-device-import-task.html)
- [list-event-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-event-configurations.html)
- [list-fuota-tasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-fuota-tasks.html)
- [list-multicast-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-multicast-groups.html)
- [list-multicast-groups-by-fuota-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-multicast-groups-by-fuota-task.html)
- [list-network-analyzer-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-network-analyzer-configurations.html)
- [list-partner-accounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-partner-accounts.html)
- [list-queued-messages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-queued-messages.html)
- [list-service-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-service-profiles.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-tags-for-resource.html)
- [list-wireless-device-import-tasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-wireless-device-import-tasks.html)
- [list-wireless-devices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-wireless-devices.html)
- [list-wireless-gateway-task-definitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-wireless-gateway-task-definitions.html)
- [list-wireless-gateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-wireless-gateways.html)
- [put-resource-log-level](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/put-resource-log-level.html)
- [reset-all-resource-log-levels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/reset-all-resource-log-levels.html)
- [reset-resource-log-level](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/reset-resource-log-level.html)
- [send-data-to-multicast-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/send-data-to-multicast-group.html)
- [send-data-to-wireless-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/send-data-to-wireless-device.html)
- [start-bulk-associate-wireless-device-with-multicast-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/start-bulk-associate-wireless-device-with-multicast-group.html)
- [start-bulk-disassociate-wireless-device-from-multicast-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/start-bulk-disassociate-wireless-device-from-multicast-group.html)
- [start-fuota-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/start-fuota-task.html)
- [start-multicast-group-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/start-multicast-group-session.html)
- [start-single-wireless-device-import-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/start-single-wireless-device-import-task.html)
- [start-wireless-device-import-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/start-wireless-device-import-task.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/tag-resource.html)
- [test-wireless-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/test-wireless-device.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/untag-resource.html)
- [update-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-destination.html)
- [update-event-configuration-by-resource-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-event-configuration-by-resource-types.html)
- [update-fuota-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-fuota-task.html)
- [update-log-levels-by-resource-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-log-levels-by-resource-types.html)
- [update-metric-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-metric-configuration.html)
- [update-multicast-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-multicast-group.html)
- [update-network-analyzer-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-network-analyzer-configuration.html)
- [update-partner-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-partner-account.html)
- [update-resource-event-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-resource-event-configuration.html)
- [update-resource-position](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-resource-position.html)
- [update-wireless-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-wireless-device.html)
- [update-wireless-device-import-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-wireless-device-import-task.html)
- [update-wireless-gateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-wireless-gateway.html)