# arc-zonal-shiftÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# arc-zonal-shift

## Description

Welcome to the API Reference Guide for zonal shift and zonal autoshift in Amazon Route 53 Application Recovery Controller (ARC).

You can start a zonal shift to move traffic for a load balancer resource away from an Availability Zone to help your application recover quickly from an impairment in an Availability Zone. For example, you can recover your application from a developerâs bad code deployment or from an Amazon Web Services infrastructure failure in a single Availability Zone.

You can also configure zonal autoshift for supported load balancer resources. Zonal autoshift is a capability in ARC where you authorize Amazon Web Services to shift away application resource traffic from an Availability Zone during events, on your behalf, to help reduce your time to recovery. Amazon Web Services starts an autoshift when internal telemetry indicates that there is an Availability Zone impairment that could potentially impact customers.

To help make sure that zonal autoshift is safe for your application, you must also configure practice runs when you enable zonal autoshift for a resource. Practice runs start weekly zonal shifts for a resource, to shift traffic for the resource away from an Availability Zone. Practice runs help you to make sure, on a regular basis, that you have enough capacity in all the Availability Zones in an Amazon Web Services Region for your application to continue to operate normally when traffic for a resource is shifted away from one Availability Zone.

### Warning

Before you configure practice runs or enable zonal autoshift, we strongly recommend that you prescale your application resource capacity in all Availability Zones in the Region where your application resources are deployed. You should not rely on scaling on demand when an autoshift or practice run starts. Zonal autoshift, including practice runs, works independently, and does not wait for auto scaling actions to complete. Relying on auto scaling, instead of pre-scaling, can result in loss of availability.

If you use auto scaling to handle regular cycles of traffic, we strongly recommend that you configure the minimum capacity of your auto scaling to continue operating normally with the loss of an Availability Zone.

Be aware that ARC does not inspect the health of individual resources. Amazon Web Services only starts an autoshift when Amazon Web Services telemetry detects that there is an Availability Zone impairment that could potentially impact customers. In some cases, resources might be shifted away that are not experiencing impact.

For more information about using zonal shift and zonal autoshift, see the [Amazon Route 53 Application Recovery Controller Developer Guide](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html) .

## Available Commands

- [cancel-zonal-shift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/cancel-zonal-shift.html)
- [create-practice-run-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/create-practice-run-configuration.html)
- [delete-practice-run-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/delete-practice-run-configuration.html)
- [get-autoshift-observer-notification-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/get-autoshift-observer-notification-status.html)
- [get-managed-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/get-managed-resource.html)
- [list-autoshifts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/list-autoshifts.html)
- [list-managed-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/list-managed-resources.html)
- [list-zonal-shifts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/list-zonal-shifts.html)
- [start-zonal-shift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/start-zonal-shift.html)
- [update-autoshift-observer-notification-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/update-autoshift-observer-notification-status.html)
- [update-practice-run-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/update-practice-run-configuration.html)
- [update-zonal-autoshift-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/update-zonal-autoshift-configuration.html)
- [update-zonal-shift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/update-zonal-shift.html)