# codecommitÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# codecommit

## Description

This is the *CodeCommit API Reference* . This reference provides descriptions of the operations and data types for CodeCommit API along with usage examples.

You can use the CodeCommit API to work with the following objects:

Repositories, by calling the following:

- BatchGetRepositories , which returns information about one or more repositories associated with your Amazon Web Services account.
- CreateRepository , which creates an CodeCommit repository.
- DeleteRepository , which deletes an CodeCommit repository.
- GetRepository , which returns information about a specified repository.
- ListRepositories , which lists all CodeCommit repositories associated with your Amazon Web Services account.
- UpdateRepositoryDescription , which sets or updates the description of the repository.
- UpdateRepositoryEncryptionKey , which updates the Key Management Service encryption key used to encrypt and decrypt a repository.
- UpdateRepositoryName , which changes the name of the repository. If you change the name of a repository, no other users of that repository can access it until you send them the new HTTPS or SSH URL to use.

Branches, by calling the following:

- CreateBranch , which creates a branch in a specified repository.
- DeleteBranch , which deletes the specified branch in a repository unless it is the default branch.
- GetBranch , which returns information about a specified branch.
- ListBranches , which lists all branches for a specified repository.
- UpdateDefaultBranch , which changes the default branch for a repository.

Files, by calling the following:

- DeleteFile , which deletes the content of a specified file from a specified branch.
- GetBlob , which returns the base-64 encoded content of an individual Git blob object in a repository.
- GetFile , which returns the base-64 encoded content of a specified file.
- GetFolder , which returns the contents of a specified folder or directory.
- ListFileCommitHistory , which retrieves a list of commits and changes to a specified file.
- PutFile , which adds or modifies a single file in a specified repository and branch.

Commits, by calling the following:

- BatchGetCommits , which returns information about one or more commits in a repository.
- CreateCommit , which creates a commit for changes to a repository.
- GetCommit , which returns information about a commit, including commit messages and author and committer information.
- GetDifferences , which returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference).

Merges, by calling the following:

- BatchDescribeMergeConflicts , which returns information about conflicts in a merge between commits in a repository.
- CreateUnreferencedMergeCommit , which creates an unreferenced commit between two branches or commits for the purpose of comparing them and identifying any potential conflicts.
- DescribeMergeConflicts , which returns information about merge conflicts between the base, source, and destination versions of a file in a potential merge.
- GetMergeCommit , which returns information about the merge between a source and destination commit.
- GetMergeConflicts , which returns information about merge conflicts between the source and destination branch in a pull request.
- GetMergeOptions , which returns information about the available merge options between two branches or commit specifiers.
- MergeBranchesByFastForward , which merges two branches using the fast-forward merge option.
- MergeBranchesBySquash , which merges two branches using the squash merge option.
- MergeBranchesByThreeWay , which merges two branches using the three-way merge option.

Pull requests, by calling the following:

- CreatePullRequest , which creates a pull request in a specified repository.
- CreatePullRequestApprovalRule , which creates an approval rule for a specified pull request.
- DeletePullRequestApprovalRule , which deletes an approval rule for a specified pull request.
- DescribePullRequestEvents , which returns information about one or more pull request events.
- EvaluatePullRequestApprovalRules , which evaluates whether a pull request has met all the conditions specified in its associated approval rules.
- GetCommentsForPullRequest , which returns information about comments on a specified pull request.
- GetPullRequest , which returns information about a specified pull request.
- GetPullRequestApprovalStates , which returns information about the approval states for a specified pull request.
- GetPullRequestOverrideState , which returns information about whether approval rules have been set aside (overriden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.
- ListPullRequests , which lists all pull requests for a repository.
- MergePullRequestByFastForward , which merges the source destination branch of a pull request into the specified destination branch for that pull request using the fast-forward merge option.
- MergePullRequestBySquash , which merges the source destination branch of a pull request into the specified destination branch for that pull request using the squash merge option.
- MergePullRequestByThreeWay , which merges the source destination branch of a pull request into the specified destination branch for that pull request using the three-way merge option.
- OverridePullRequestApprovalRules , which sets aside all approval rule requirements for a pull request.
- PostCommentForPullRequest , which posts a comment to a pull request at the specified line, file, or request.
- UpdatePullRequestApprovalRuleContent , which updates the structure of an approval rule for a pull request.
- UpdatePullRequestApprovalState , which updates the state of an approval on a pull request.
- UpdatePullRequestDescription , which updates the description of a pull request.
- UpdatePullRequestStatus , which updates the status of a pull request.
- UpdatePullRequestTitle , which updates the title of a pull request.

Approval rule templates, by calling the following:

- AssociateApprovalRuleTemplateWithRepository , which associates a template with a specified repository. After the template is associated with a repository, CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repository.
- BatchAssociateApprovalRuleTemplateWithRepositories , which associates a template with one or more specified repositories. After the template is associated with a repository, CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repositories.
- BatchDisassociateApprovalRuleTemplateFromRepositories , which removes the association between a template and specified repositories so that approval rules based on the template are not automatically created when pull requests are created in those repositories.
- CreateApprovalRuleTemplate , which creates a template for approval rules that can then be associated with one or more repositories in your Amazon Web Services account.
- DeleteApprovalRuleTemplate , which deletes the specified template. It does not remove approval rules on pull requests already created with the template.
- DisassociateApprovalRuleTemplateFromRepository , which removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository.
- GetApprovalRuleTemplate , which returns information about an approval rule template.
- ListApprovalRuleTemplates , which lists all approval rule templates in the Amazon Web Services Region in your Amazon Web Services account.
- ListAssociatedApprovalRuleTemplatesForRepository , which lists all approval rule templates that are associated with a specified repository.
- ListRepositoriesForApprovalRuleTemplate , which lists all repositories associated with the specified approval rule template.
- UpdateApprovalRuleTemplateDescription , which updates the description of an approval rule template.
- UpdateApprovalRuleTemplateName , which updates the name of an approval rule template.
- UpdateApprovalRuleTemplateContent , which updates the content of an approval rule template.

Comments in a repository, by calling the following:

- DeleteCommentContent , which deletes the content of a comment on a commit in a repository.
- GetComment , which returns information about a comment on a commit.
- GetCommentReactions , which returns information about emoji reactions to comments.
- GetCommentsForComparedCommit , which returns information about comments on the comparison between two commit specifiers in a repository.
- PostCommentForComparedCommit , which creates a comment on the comparison between two commit specifiers in a repository.
- PostCommentReply , which creates a reply to a comment.
- PutCommentReaction , which creates or updates an emoji reaction to a comment.
- UpdateComment , which updates the content of a comment on a commit in a repository.

Tags used to tag resources in CodeCommit (not Git tags), by calling the following:

- ListTagsForResource , which gets information about Amazon Web Servicestags for a specified Amazon Resource Name (ARN) in CodeCommit.
- TagResource , which adds or updates tags for a resource in CodeCommit.
- UntagResource , which removes tags for a resource in CodeCommit.

Triggers, by calling the following:

- GetRepositoryTriggers , which returns information about triggers configured for a repository.
- PutRepositoryTriggers , which replaces all triggers for a repository and can be used to create or delete triggers.
- TestRepositoryTriggers , which tests the functionality of a repository trigger by sending data to the trigger target.

For information about how to use CodeCommit, see the [CodeCommit User Guide](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) .

## Available Commands

- [associate-approval-rule-template-with-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/associate-approval-rule-template-with-repository.html)
- [batch-associate-approval-rule-template-with-repositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-associate-approval-rule-template-with-repositories.html)
- [batch-describe-merge-conflicts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-describe-merge-conflicts.html)
- [batch-disassociate-approval-rule-template-from-repositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-disassociate-approval-rule-template-from-repositories.html)
- [batch-get-commits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-get-commits.html)
- [batch-get-repositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-get-repositories.html)
- [create-approval-rule-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-approval-rule-template.html)
- [create-branch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-branch.html)
- [create-commit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-commit.html)
- [create-pull-request](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-pull-request.html)
- [create-pull-request-approval-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-pull-request-approval-rule.html)
- [create-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-repository.html)
- [create-unreferenced-merge-commit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-unreferenced-merge-commit.html)
- [credential-helper](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/credential-helper/index.html)
- [delete-approval-rule-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-approval-rule-template.html)
- [delete-branch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-branch.html)
- [delete-comment-content](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-comment-content.html)
- [delete-file](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-file.html)
- [delete-pull-request-approval-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-pull-request-approval-rule.html)
- [delete-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-repository.html)
- [describe-merge-conflicts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/describe-merge-conflicts.html)
- [describe-pull-request-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/describe-pull-request-events.html)
- [disassociate-approval-rule-template-from-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/disassociate-approval-rule-template-from-repository.html)
- [evaluate-pull-request-approval-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/evaluate-pull-request-approval-rules.html)
- [get-approval-rule-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-approval-rule-template.html)
- [get-blob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-blob.html)
- [get-branch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-branch.html)
- [get-comment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comment.html)
- [get-comment-reactions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comment-reactions.html)
- [get-comments-for-compared-commit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comments-for-compared-commit.html)
- [get-comments-for-pull-request](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comments-for-pull-request.html)
- [get-commit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-commit.html)
- [get-differences](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-differences.html)
- [get-file](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-file.html)
- [get-folder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-folder.html)
- [get-merge-commit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-merge-commit.html)
- [get-merge-conflicts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-merge-conflicts.html)
- [get-merge-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-merge-options.html)
- [get-pull-request](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request.html)
- [get-pull-request-approval-states](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request-approval-states.html)
- [get-pull-request-override-state](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request-override-state.html)
- [get-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-repository.html)
- [get-repository-triggers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-repository-triggers.html)
- [list-approval-rule-templates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-approval-rule-templates.html)
- [list-associated-approval-rule-templates-for-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-associated-approval-rule-templates-for-repository.html)
- [list-branches](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-branches.html)
- [list-file-commit-history](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-file-commit-history.html)
- [list-pull-requests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-pull-requests.html)
- [list-repositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-repositories.html)
- [list-repositories-for-approval-rule-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-repositories-for-approval-rule-template.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-tags-for-resource.html)
- [merge-branches-by-fast-forward](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-branches-by-fast-forward.html)
- [merge-branches-by-squash](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-branches-by-squash.html)
- [merge-branches-by-three-way](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-branches-by-three-way.html)
- [merge-pull-request-by-fast-forward](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-pull-request-by-fast-forward.html)
- [merge-pull-request-by-squash](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-pull-request-by-squash.html)
- [merge-pull-request-by-three-way](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-pull-request-by-three-way.html)
- [override-pull-request-approval-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/override-pull-request-approval-rules.html)
- [post-comment-for-compared-commit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/post-comment-for-compared-commit.html)
- [post-comment-for-pull-request](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/post-comment-for-pull-request.html)
- [post-comment-reply](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/post-comment-reply.html)
- [put-comment-reaction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/put-comment-reaction.html)
- [put-file](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/put-file.html)
- [put-repository-triggers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/put-repository-triggers.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/tag-resource.html)
- [test-repository-triggers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/test-repository-triggers.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/untag-resource.html)
- [update-approval-rule-template-content](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-approval-rule-template-content.html)
- [update-approval-rule-template-description](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-approval-rule-template-description.html)
- [update-approval-rule-template-name](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-approval-rule-template-name.html)
- [update-comment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-comment.html)
- [update-default-branch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-default-branch.html)
- [update-pull-request-approval-rule-content](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-approval-rule-content.html)
- [update-pull-request-approval-state](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-approval-state.html)
- [update-pull-request-description](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-description.html)
- [update-pull-request-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-status.html)
- [update-pull-request-title](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-title.html)
- [update-repository-description](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-repository-description.html)
- [update-repository-encryption-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-repository-encryption-key.html)
- [update-repository-name](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-repository-name.html)