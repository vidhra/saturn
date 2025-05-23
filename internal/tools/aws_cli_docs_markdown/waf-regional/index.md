# waf-regionalÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# waf-regional

## Description

### Note

This is **AWS WAF Classic Regional** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

This is the *AWS WAF Regional Classic API Reference* for using AWS WAF Classic with the AWS resources, Elastic Load Balancing (ELB) Application Load Balancers and API Gateway APIs. The AWS WAF Classic actions and data types listed in the reference are available for protecting Elastic Load Balancing (ELB) Application Load Balancers and API Gateway APIs. You can use these actions and data types by means of the endpoints listed in [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#waf_region) . This guide is for developers who need detailed information about the AWS WAF Classic API actions, data types, and errors. For detailed information about AWS WAF Classic features and an overview of how to use the AWS WAF Classic API, see the [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

## Available Commands

- [associate-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/associate-web-acl.html)
- [create-byte-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-byte-match-set.html)
- [create-geo-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-geo-match-set.html)
- [create-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-ip-set.html)
- [create-rate-based-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-rate-based-rule.html)
- [create-regex-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-regex-match-set.html)
- [create-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-regex-pattern-set.html)
- [create-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-rule.html)
- [create-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-rule-group.html)
- [create-size-constraint-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-size-constraint-set.html)
- [create-sql-injection-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-sql-injection-match-set.html)
- [create-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-web-acl.html)
- [create-web-acl-migration-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-web-acl-migration-stack.html)
- [create-xss-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-xss-match-set.html)
- [delete-byte-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-byte-match-set.html)
- [delete-geo-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-geo-match-set.html)
- [delete-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-ip-set.html)
- [delete-logging-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-logging-configuration.html)
- [delete-permission-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-permission-policy.html)
- [delete-rate-based-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-rate-based-rule.html)
- [delete-regex-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-regex-match-set.html)
- [delete-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-regex-pattern-set.html)
- [delete-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-rule.html)
- [delete-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-rule-group.html)
- [delete-size-constraint-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-size-constraint-set.html)
- [delete-sql-injection-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-sql-injection-match-set.html)
- [delete-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-web-acl.html)
- [delete-xss-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-xss-match-set.html)
- [disassociate-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/disassociate-web-acl.html)
- [get-byte-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-byte-match-set.html)
- [get-change-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-change-token.html)
- [get-change-token-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-change-token-status.html)
- [get-geo-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-geo-match-set.html)
- [get-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-ip-set.html)
- [get-logging-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-logging-configuration.html)
- [get-permission-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-permission-policy.html)
- [get-rate-based-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-rate-based-rule.html)
- [get-rate-based-rule-managed-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-rate-based-rule-managed-keys.html)
- [get-regex-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-regex-match-set.html)
- [get-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-regex-pattern-set.html)
- [get-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-rule.html)
- [get-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-rule-group.html)
- [get-sampled-requests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-sampled-requests.html)
- [get-size-constraint-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-size-constraint-set.html)
- [get-sql-injection-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-sql-injection-match-set.html)
- [get-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-web-acl.html)
- [get-web-acl-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-web-acl-for-resource.html)
- [get-xss-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-xss-match-set.html)
- [list-activated-rules-in-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-activated-rules-in-rule-group.html)
- [list-byte-match-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-byte-match-sets.html)
- [list-geo-match-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-geo-match-sets.html)
- [list-ip-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-ip-sets.html)
- [list-logging-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-logging-configurations.html)
- [list-rate-based-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-rate-based-rules.html)
- [list-regex-match-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-regex-match-sets.html)
- [list-regex-pattern-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-regex-pattern-sets.html)
- [list-resources-for-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-resources-for-web-acl.html)
- [list-rule-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-rule-groups.html)
- [list-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-rules.html)
- [list-size-constraint-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-size-constraint-sets.html)
- [list-sql-injection-match-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-sql-injection-match-sets.html)
- [list-subscribed-rule-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-subscribed-rule-groups.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-tags-for-resource.html)
- [list-web-acls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-web-acls.html)
- [list-xss-match-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-xss-match-sets.html)
- [put-logging-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/put-logging-configuration.html)
- [put-permission-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/put-permission-policy.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/untag-resource.html)
- [update-byte-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-byte-match-set.html)
- [update-geo-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-geo-match-set.html)
- [update-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-ip-set.html)
- [update-rate-based-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-rate-based-rule.html)
- [update-regex-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-regex-match-set.html)
- [update-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-regex-pattern-set.html)
- [update-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-rule.html)
- [update-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-rule-group.html)
- [update-size-constraint-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-size-constraint-set.html)
- [update-sql-injection-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-sql-injection-match-set.html)
- [update-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-web-acl.html)
- [update-xss-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-xss-match-set.html)