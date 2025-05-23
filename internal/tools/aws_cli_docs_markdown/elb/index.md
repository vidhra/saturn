# elbÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# elb

## Description

A load balancer can distribute incoming traffic across your EC2 instances. This enables you to increase the availability of your application. The load balancer also monitors the health of its registered instances and ensures that it routes traffic only to healthy instances. You configure your load balancer to accept incoming traffic by specifying one or more listeners, which are configured with a protocol and port number for connections from clients to the load balancer and a protocol and port number for connections from the load balancer to the instances.

Elastic Load Balancing supports three types of load balancers: Application Load Balancers, Network Load Balancers, and Classic Load Balancers. You can select a load balancer based on your application needs. For more information, see the [Elastic Load Balancing User Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/) .

This reference covers the 2012-06-01 API, which supports Classic Load Balancers. The 2015-12-01 API supports Application Load Balancers and Network Load Balancers.

To get started, create a load balancer with one or more listeners using  CreateLoadBalancer . Register your instances with the load balancer using  RegisterInstancesWithLoadBalancer .

All Elastic Load Balancing operations are *idempotent* , which means that they complete at most one time. If you repeat an operation, it succeeds with a 200 OK response code.

## Available Commands

- [add-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/add-tags.html)
- [apply-security-groups-to-load-balancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/apply-security-groups-to-load-balancer.html)
- [attach-load-balancer-to-subnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/attach-load-balancer-to-subnets.html)
- [configure-health-check](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/configure-health-check.html)
- [create-app-cookie-stickiness-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-app-cookie-stickiness-policy.html)
- [create-lb-cookie-stickiness-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-lb-cookie-stickiness-policy.html)
- [create-load-balancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer.html)
- [create-load-balancer-listeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer-listeners.html)
- [create-load-balancer-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer-policy.html)
- [delete-load-balancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer.html)
- [delete-load-balancer-listeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer-listeners.html)
- [delete-load-balancer-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer-policy.html)
- [deregister-instances-from-load-balancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/deregister-instances-from-load-balancer.html)
- [describe-account-limits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-account-limits.html)
- [describe-instance-health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-instance-health.html)
- [describe-load-balancer-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-attributes.html)
- [describe-load-balancer-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-policies.html)
- [describe-load-balancer-policy-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-policy-types.html)
- [describe-load-balancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancers.html)
- [describe-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-tags.html)
- [detach-load-balancer-from-subnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/detach-load-balancer-from-subnets.html)
- [disable-availability-zones-for-load-balancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/disable-availability-zones-for-load-balancer.html)
- [enable-availability-zones-for-load-balancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/enable-availability-zones-for-load-balancer.html)
- [modify-load-balancer-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/modify-load-balancer-attributes.html)
- [register-instances-with-load-balancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/register-instances-with-load-balancer.html)
- [remove-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/remove-tags.html)
- [set-load-balancer-listener-ssl-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-listener-ssl-certificate.html)
- [set-load-balancer-policies-for-backend-server](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-policies-for-backend-server.html)
- [set-load-balancer-policies-of-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-policies-of-listener.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/wait/index.html)