# wafÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# waf

## Description

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

This is the *AWS WAF Classic API Reference* for using AWS WAF Classic with Amazon CloudFront. The AWS WAF Classic actions and data types listed in the reference are available for protecting Amazon CloudFront distributions. You can use these actions and data types via the endpoint *waf.amazonaws.com* . This guide is for developers who need detailed information about the AWS WAF Classic API actions, data types, and errors. For detailed information about AWS WAF Classic features and an overview of how to use the AWS WAF Classic API, see the [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

## Available Commands

- [create-byte-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-byte-match-set.html)
- [create-geo-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-geo-match-set.html)
- [create-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-ip-set.html)
- [create-rate-based-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rate-based-rule.html)
- [create-regex-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-regex-match-set.html)
- [create-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-regex-pattern-set.html)
- [create-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rule.html)
- [create-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rule-group.html)
- [create-size-constraint-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-size-constraint-set.html)
- [create-sql-injection-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-sql-injection-match-set.html)
- [create-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-web-acl.html)
- [create-web-acl-migration-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-web-acl-migration-stack.html)
- [create-xss-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-xss-match-set.html)
- [delete-byte-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-byte-match-set.html)
- [delete-geo-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-geo-match-set.html)
- [delete-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-ip-set.html)
- [delete-logging-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-logging-configuration.html)
- [delete-permission-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-permission-policy.html)
- [delete-rate-based-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-rate-based-rule.html)
- [delete-regex-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-regex-match-set.html)
- [delete-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-regex-pattern-set.html)
- [delete-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-rule.html)
- [delete-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-rule-group.html)
- [delete-size-constraint-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-size-constraint-set.html)
- [delete-sql-injection-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-sql-injection-match-set.html)
- [delete-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-web-acl.html)
- [delete-xss-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-xss-match-set.html)
- [get-byte-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-byte-match-set.html)
- [get-change-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-change-token.html)
- [get-change-token-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-change-token-status.html)
- [get-geo-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-geo-match-set.html)
- [get-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-ip-set.html)
- [get-logging-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-logging-configuration.html)
- [get-permission-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-permission-policy.html)
- [get-rate-based-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rate-based-rule.html)
- [get-rate-based-rule-managed-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rate-based-rule-managed-keys.html)
- [get-regex-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-regex-match-set.html)
- [get-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-regex-pattern-set.html)
- [get-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rule.html)
- [get-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rule-group.html)
- [get-sampled-requests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-sampled-requests.html)
- [get-size-constraint-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-size-constraint-set.html)
- [get-sql-injection-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-sql-injection-match-set.html)
- [get-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-web-acl.html)
- [get-xss-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-xss-match-set.html)
- [list-activated-rules-in-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-activated-rules-in-rule-group.html)
- [list-byte-match-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-byte-match-sets.html)
- [list-geo-match-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-geo-match-sets.html)
- [list-ip-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-ip-sets.html)
- [list-logging-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-logging-configurations.html)
- [list-rate-based-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rate-based-rules.html)
- [list-regex-match-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-regex-match-sets.html)
- [list-regex-pattern-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-regex-pattern-sets.html)
- [list-rule-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rule-groups.html)
- [list-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rules.html)
- [list-size-constraint-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-size-constraint-sets.html)
- [list-sql-injection-match-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-sql-injection-match-sets.html)
- [list-subscribed-rule-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-subscribed-rule-groups.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-tags-for-resource.html)
- [list-web-acls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-web-acls.html)
- [list-xss-match-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-xss-match-sets.html)
- [put-logging-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/put-logging-configuration.html)
- [put-permission-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/put-permission-policy.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/untag-resource.html)
- [update-byte-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-byte-match-set.html)
- [update-geo-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-geo-match-set.html)
- [update-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-ip-set.html)
- [update-rate-based-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rate-based-rule.html)
- [update-regex-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-regex-match-set.html)
- [update-regex-pattern-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-regex-pattern-set.html)
- [update-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rule.html)
- [update-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rule-group.html)
- [update-size-constraint-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-size-constraint-set.html)
- [update-sql-injection-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-sql-injection-match-set.html)
- [update-web-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-web-acl.html)
- [update-xss-match-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-xss-match-set.html)