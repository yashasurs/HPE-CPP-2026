import re
import spacy
import tiktoken


# MODEL

# Transformer parsing is used for AKU extraction. Chunking uses a blank sentencizer
NLP = spacy.load("en_core_web_trf", disable=["ner"])
NLP.max_length = 2_000_000

SENT_NLP = spacy.blank("en")
SENT_NLP.add_pipe("sentencizer")
SENT_NLP.max_length = 2_000_000

TOKENIZER = tiktoken.get_encoding("cl100k_base")

# CONFIG

MIN_SENT_WORDS = 4
MAX_SENT_WORDS = 120
MIN_CHUNK_TOKENS = 120
TARGET_CHUNK_TOKENS = 650
MAX_CHUNK_TOKENS = 850
OVERLAP_TOKENS = 120
AKU_BATCH_SIZE = 8
MAX_AKUS_PER_CHUNK = 12


# FILTER RULES


BAD_SUBJECTS = {
    "you", "your", "we", "our", "it", "its", "they", "them", "this",
    "that", "these", "those", "who", "which", "the service",
    "the request", "this request", "the response", "this response",
    "this section", "the following", "example", "request", "name",
    "value", "values", "data",
}

BAD_OBJECTS = {
    "value", "data", "thing", "information", "example", "parameter",
    "parameters",
}

GENERIC_ENTITY_PHRASES = {
    "this value", "that value", "the value", "these values", "valid values",
    "this parameter", "that parameter", "the parameter", "these parameters",
    "this request", "that request", "the request", "this response",
    "that response", "the response", "the following", "this operation",
    "that operation", "the operation", "this action", "that action",
    "the action", "the service", "this service", "the resource",
    "this resource", "the user", "this user",
}

WEAK_ENTITY_HEADS = {
    "type", "types", "name", "names", "value", "values", "data",
    "example", "examples", "content", "contents", "description",
    "descriptions", "information", "details", "result", "results",
}

BAD_VERBS = {
    "be", "have", "do", "make", "use", "is", "are", "was", "were",
    "has", "had", "can", "could", "will", "would", "should", "may",
    "might", "get", "see", "show",
}

GOOD_VERBS = {
    "accept", "add", "allow", "analyze", "apply", "associate",
    "attach", "authenticate", "authorize", "back", "backup", "calculate", "call",
    "capture", "collect", "configure", "connect", "contain", "copy",
    "create", "define", "delete", "deliver", "deny", "deploy", "describe",
    "detach", "disable", "discover", "enable", "encrypt", "enforce",
    "evaluate", "execute", "export", "filter", "generate", "grant",
    "identify", "import", "include", "invoke", "launch", "list", "load",
    "log", "manage", "monitor", "notify", "own", "perform", "prevent",
    "process", "protect", "publish", "query", "read", "receive",
    "record", "replicate", "require", "resolve", "restore", "retrieve",
    "route", "run", "scale", "schedule", "send", "sign", "specify",
    "start", "stop", "store", "stream", "submit", "support", "tag",
    "track", "trigger", "update", "upload", "validate", "verify",
}

VERB_NORMALIZATION = {
    "add": "create",
    "allocate": "create",
    "analyze": "evaluate",
    "back": "backup",
    "build": "create",
    "change": "update",
    "check": "validate",
    "collect": "record",
    "configure": "configure",
    "connect": "connect",
    "copy": "copy",
    "delete": "delete",
    "deploy": "deploy",
    "describe": "retrieve",
    "disable": "disable",
    "discover": "discover",
    "enable": "enable",
    "execute": "run",
    "generate": "create",
    "invoke": "invoke",
    "launch": "start",
    "list": "retrieve",
    "modify": "update",
    "monitor": "monitor",
    "publish": "publish",
    "put": "create",
    "read": "retrieve",
    "receive": "receive",
    "remove": "delete",
    "replicate": "replicate",
    "restore": "restore",
    "retrieve": "retrieve",
    "run": "run",
    "send": "send",
    "start": "start",
    "stop": "stop",
    "store": "store",
    "submit": "submit",
    "tag": "tag",
    "trigger": "trigger",
    "untag": "delete",
    "update": "update",
    "upload": "upload",
    "validate": "validate",
    "verify": "validate",
}

ACTION_PREFIXES = {
    "Accept": "accept",
    "Add": "create",
    "Allocate": "create",
    "Analyze": "evaluate",
    "Associate": "associate",
    "Attach": "attach",
    "Authorize": "authorize",
    "Cancel": "delete",
    "Create": "create",
    "Delete": "delete",
    "Deregister": "delete",
    "Describe": "retrieve",
    "Detach": "detach",
    "Disable": "disable",
    "Disassociate": "detach",
    "Enable": "enable",
    "Get": "retrieve",
    "Invoke": "invoke",
    "List": "retrieve",
    "Modify": "update",
    "Put": "create",
    "Register": "create",
    "Remove": "delete",
    "Restore": "restore",
    "Revoke": "delete",
    "Run": "start",
    "Start": "start",
    "Stop": "stop",
    "Tag": "tag",
    "Untag": "delete",
    "Update": "update",
}

RESOURCE_QUALIFIERS = {
    "alarm": "CloudWatch alarm resource",
    "alias": "Lambda alias resource",
    "archive": "S3 Glacier archive resource",
    "bucket": "S3 bucket resource",
    "change set": "CloudFormation change set resource",
    "cluster": "RDS DB cluster resource",
    "dashboard": "CloudWatch dashboard resource",
    "db cluster": "RDS DB cluster resource",
    "db instance": "RDS DB instance resource",
    "event source mapping": "Lambda event source mapping resource",
    "function": "Lambda function resource",
    "group": "IAM group resource",
    "image": "EC2 AMI resource",
    "instance": "EC2 instance resource",
    "key pair": "EC2 key pair resource",
    "layer version": "Lambda layer version resource",
    "log group": "CloudWatch log group resource",
    "log stream": "CloudWatch log stream resource",
    "network interface": "EC2 network interface resource",
    "object": "S3 object resource",
    "policy": "IAM policy resource",
    "role": "IAM role resource",
    "route": "VPC route resource",
    "route table": "VPC route table resource",
    "rule": "EventBridge rule resource",
    "security group": "EC2 security group resource",
    "snapshot": "EC2 snapshot resource",
    "stack": "CloudFormation stack resource",
    "stack set": "CloudFormation stack set resource",
    "subnet": "VPC subnet resource",
    "template": "CloudFormation template resource",
    "user": "IAM user resource",
    "volume": "EC2 volume resource",
    "vpc": "VPC resource",
}

DOMAIN_TERMS = {
    # AWS-wide
    "aws", "amazon web services", "account", "accounts", "action",
    "actions", "region",
    "regions", "availability zone", "availability zones", "resource",
    "resources", "tag", "tags", "arn", "amazon resource name",
    "service", "services", "console", "cli", "sdk", "api", "apis",
    "endpoint", "endpoints", "request", "requests", "response",
    "responses", "header", "headers", "quota", "quotas", "limit",
    "limits", "operation", "operations", "event", "events", "metric", "metrics", "alarm", "alarms",
    "log", "logs", "permission", "permissions", "policy", "policies",
    "role", "roles", "user", "users", "group", "groups", "principal",
    "principals", "identity", "identities", "credential", "credentials",
    "session", "sessions", "token", "tokens", "security", "encryption",
    "kms", "key", "keys", "certificate", "certificates", "secret",
    "secrets", "signature", "condition", "conditions",

    # S3 / Glacier
    "s3", "amazon s3", "simple storage service", "bucket", "buckets",
    "object", "objects", "acl", "acls", "access point", "access points",
    "versioning", "lifecycle", "multipart", "upload", "uploads",
    "replication", "storage class", "storage classes", "checksum",
    "checksums", "glacier", "vault", "vaults", "archive", "archives",
    "outposts",

    # EC2
    "ec2", "amazon ec2", "instance", "instances", "ami", "amis",
    "image", "images", "volume", "volumes", "snapshot", "snapshots",
    "ebs", "elastic block store", "security group", "security groups",
    "key pair", "key pairs", "network interface", "network interfaces",
    "elastic ip", "elastic ips", "placement group", "placement groups",
    "launch template", "launch templates", "auto scaling", "enclave",
    "enclaves",

    # VPC / networking
    "vpc", "vpcs", "subnet", "subnets", "route table", "route tables",
    "route", "routes", "internet gateway", "internet gateways",
    "nat gateway", "nat gateways", "transit gateway", "transit gateways",
    "customer gateway", "customer gateways", "vpn", "vpn connection",
    "cidr", "ipv4", "ipv6", "ipam", "private link", "privatelink",
    "vpc lattice", "cloud wan", "network manager", "network access scope",
    "network access analyzer", "reachability analyzer", "flow logs",
    "network firewall", "load balancer", "load balancers", "elb", "alb",
    "nlb", "target group", "target groups", "listener", "listeners",
    "dns", "hosted zone",

    # IAM / STS / Access Analyzer / Roles Anywhere
    "iam", "sts", "access analyzer", "roles anywhere", "trust policy",
    "trust policies", "identity policy", "identity policies",
    "resource policy", "resource policies", "managed policy",
    "managed policies", "inline policy", "inline policies", "assume role",
    "federation", "saml", "oidc", "mfa", "access key", "access keys",
    "temporary credentials", "permission set", "service principal",

    # Lambda / serverless
    "lambda", "aws lambda", "function", "functions", "runtime",
    "runtimes", "handler", "handlers", "layer", "layers", "alias",
    "aliases", "version", "versions", "event source", "event sources",
    "event source mapping", "event source mappings", "trigger",
    "triggers", "concurrency", "provisioned concurrency", "execution role",
    "destination", "destinations", "dead-letter queue", "snapstart",
    "serverless",

    # RDS / Aurora / databases
    "rds", "amazon rds", "aurora", "database", "databases",
    "db instance", "db instances", "db cluster", "db clusters",
    "db engine", "db engines", "parameter group", "parameter groups",
    "option group", "option groups", "subnet group", "subnet groups",
    "read replica", "read replicas", "backup", "backups",
    "restore", "snapshot", "snapshots", "performance insights",
    "postgresql", "mysql", "mariadb", "oracle", "sql server",
    "rds data api",

    # CloudWatch / EventBridge / observability
    "cloudwatch", "amazon cloudwatch", "cloudwatch logs",
    "log group", "log groups", "log stream", "log streams",
    "metric alarm", "metric alarms", "composite alarm",
    "composite alarms", "dashboard", "dashboards", "namespace",
    "namespaces", "dimension", "dimensions", "eventbridge",
    "event bus", "event buses", "rule", "rules", "target", "targets",
    "synthetics", "canary", "canaries", "rum", "application signals",
    "app insights", "internet monitor", "network flow monitor",
    "observability", "aiops", "trace", "traces",

    # CloudFormation / IaC
    "cloudformation", "aws cloudformation", "stack", "stacks",
    "stack set", "stack sets", "template", "templates", "change set",
    "change sets", "resource type", "resource types", "drift",
    "hook", "hooks", "cloudformation guard", "guard rule",
    "guard rules", "cfn", "cfn cli", "registry", "macro", "macros",
}

GENERIC_DOMAIN_TERMS = {
    "aws", "amazon web services", "account", "accounts", "action", "actions",
    "region", "regions", "resource", "resources", "service", "services",
    "console", "cli", "sdk", "api", "apis", "endpoint", "endpoints",
    "request", "requests", "response", "responses", "header", "headers",
    "operation", "operations", "event", "events", "permission",
    "permissions", "policy", "policies", "role", "roles", "user", "users",
    "group", "groups", "principal", "principals", "identity", "identities",
    "credential", "credentials", "session", "sessions", "token", "tokens",
    "security", "condition", "conditions", "tag", "tags", "limit", "limits",
    "quota", "quotas",
}

SPECIFIC_DOMAIN_TERMS = DOMAIN_TERMS - GENERIC_DOMAIN_TERMS

LOW_VALUE_SECTION_TITLES = {
    "request syntax", "response syntax", "examples", "sample request",
    "sample response", "request body", "response body", "request parameters",
    "response elements", "uri request parameters", "errors", "see also",
}

NOISE_PATTERNS = [
    re.compile(r".*\.{10,}.*\n"),
    re.compile(r"API Version \d{4}-\d{2}-\d{2}.*\n"),
    re.compile(r"Copyright.*\n", re.IGNORECASE),
    re.compile(r"Amazon'?s trademarks.*\n", re.IGNORECASE),
    re.compile(r"^\s*Page \d+.*$", re.MULTILINE),
]

WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9-]*")
CODE_RE = re.compile(r"[=(){}$]|::|->|\b(client|sdk|new|const|class)\b", re.IGNORECASE)
HTTP_RE = re.compile(
    r"\b(http|status|response|error|code|ok|not found|denied|success)\b",
    re.IGNORECASE,
)
DOMAIN_RE = re.compile(
    r"\b(" + "|".join(re.escape(t) for t in sorted(DOMAIN_TERMS, key=len, reverse=True)) + r")\b",
    re.IGNORECASE,
)
SPECIFIC_DOMAIN_RE = re.compile(
    r"\b("
    + "|".join(re.escape(t) for t in sorted(SPECIFIC_DOMAIN_TERMS, key=len, reverse=True))
    + r")\b",
    re.IGNORECASE,
)
