# rbinÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# rbin

## Description

This is the *Recycle Bin API Reference* . This documentation provides descriptions and syntax for each of the actions and data types in Recycle Bin.

Recycle Bin is a resource recovery feature that enables you to restore accidentally deleted snapshots and EBS-backed AMIs. When using Recycle Bin, if your resources are deleted, they are retained in the Recycle Bin for a time period that you specify.

You can restore a resource from the Recycle Bin at any time before its retention period expires. After you restore a resource from the Recycle Bin, the resource is removed from the Recycle Bin, and you can then use it in the same way you use any other resource of that type in your account. If the retention period expires and the resource is not restored, the resource is permanently deleted from the Recycle Bin and is no longer available for recovery. For more information about Recycle Bin, see [Recycle Bin](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin.html) in the *Amazon Elastic Compute Cloud User Guide* .

## Available Commands

- [create-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/create-rule.html)
- [delete-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/delete-rule.html)
- [get-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/get-rule.html)
- [list-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/list-rules.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/list-tags-for-resource.html)
- [lock-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/lock-rule.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/tag-resource.html)
- [unlock-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/unlock-rule.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/untag-resource.html)
- [update-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/update-rule.html)