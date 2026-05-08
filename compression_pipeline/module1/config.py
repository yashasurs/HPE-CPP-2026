import re
import spacy
import tiktoken

NLP = spacy.load("en_core_web_trf", disable=["ner"])
NLP.max_length = 2_000_000

SENT_NLP = spacy.blank("en")
SENT_NLP.add_pipe("sentencizer")
SENT_NLP.max_length = 2_000_000

TOKENIZER = tiktoken.get_encoding("cl100k_base")

MIN_SENT_WORDS = 4
MAX_SENT_WORDS = 120
MIN_CHUNK_TOKENS = 120
TARGET_CHUNK_TOKENS = 650
MAX_CHUNK_TOKENS = 850
OVERLAP_TOKENS = 120

MARKDOWN_HEADERS = [("#", "H1"), ("##", "H2"), ("###", "H3")]
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
MIN_TOKEN_COUNT = 75

AKU_BATCH_SIZE = 8
MAX_AKUS_PER_CHUNK = 8

ENCODING_FIXES = {
    "\ufb01": "fi",
    "\ufb02": "fl",
    "\u2013": "-",
    "\u2014": "-",
}

NOISE_PATTERNS = [
    r"Table of Contents",
    r"Amazon Simple Storage Service API Reference",
    r"API Reference",
    r"Copyright © .*",
    r"Amazon's trademarks.*",
    r"All other trademarks.*",
    r"API Version \d{4}-\d{2}-\d{2}",
]

REPEATED_LINE_THRESHOLD = 5

TECHNICAL_PREFIXES = (
    "x-amz-",
    "GET ",
    "PUT ",
    "POST ",
    "DELETE ",
    "HEAD ",
    "PATCH ",
    "HTTP/",
    "AWS",
    "IAM",
    "S3",
    "KMS",
    "ARN",
    "--",
    "#{",
    "${",
)

TECHNICAL_PATTERNS = re.compile(
    r"^([A-Z][a-z]+[A-Z]|"
    r"[a-z]+-[a-z]+"
    r"|\d+(\.\d+)+"
    r"|[A-Z]{2,}"
    r"|[a-z]+:[A-Z]"
    r'|\S+=["\'\w])'
)

MAX_NP_WORDS = 10

VERB_MAP = {
    "have": "HAS", "require": "REQUIRES", "need": "REQUIRES",
    "use": "USES", "store": "STORES", "create": "CREATES",
    "generate": "CREATES", "allow": "ALLOWS", "grant": "GRANTS",
    "enable": "ENABLES", "disable": "DISABLES", "send": "SENDS",
    "receive": "RECEIVES", "define": "DEFINES", "specify": "SPECIFIES",
    "limit": "LIMITS", "provide": "PROVIDES", "authenticate": "AUTHENTICATES",
    "authorize": "AUTHORIZES", "validate": "VALIDATES", "deploy": "DEPLOYS",
    "configure": "CONFIGURES", "manage": "MANAGES", "monitor": "MONITORS",
    "access": "ACCESSES", "execute": "EXECUTES", "run": "EXECUTES",
    "connect": "CONNECTS", "trigger": "TRIGGERS", "invoke": "INVOKES",
    "support": "SUPPORTS", "contain": "CONTAINS", "include": "INCLUDES",
    "expose": "EXPOSES", "route": "ROUTES", "encrypt": "ENCRYPTS",
    "handle": "HANDLES", "process": "PROCESSES", "return": "RETURNS",
    "call": "INVOKES", "attach": "ATTACHES", "associate": "ASSOCIATES",
    "block": "BLOCKS", "restrict": "RESTRICTS", "enforce": "ENFORCES",
    "register": "REGISTERS", "publish": "PUBLISHES", "subscribe": "SUBSCRIBES",
    "read": "READS", "write": "WRITES", "delete": "DELETES", "update": "UPDATES",
    "list": "LISTS", "scale": "SCALES", "cache": "CACHES", "log": "LOGS",
    "tag": "TAGS", "filter": "FILTERS", "transform": "TRANSFORMS",
    "control": "CONTROLS", "accept": "ACCEPTS",
}

COPULA_LEMMAS = {"be", "become", "remain", "represent", "constitute"}

INVALID_ENTITIES = {
    "this", "that", "it", "which", "example", "following", "section",
    "guide", "both", "all", "each", "above", "below", "here", "there",
    "note", "however", "therefore", "otherwise", "those", "these",
    "they", "them", "their", "we", "our", "you", "your", "he", "she",
    "reference", "table", "document", "topic", "page", "overview",
}

GENERIC_HEAD_NOUNS = {
    "system", "service", "feature", "data", "value", "field",
    "request", "response", "object", "resource", "result", "item",
    "type", "list", "set", "way", "method", "approach", "option",
    "information", "content", "detail", "thing", "entity", "element",
    "functionality", "behavior", "action", "process", "operation",
    "component", "part", "aspect", "property", "attribute", "parameter",
}

GENERIC_OBJECTS = {
    "data", "value", "object", "request", "response", "result",
    "information", "functionality", "behavior", "content", "detail",
    "thing", "entity", "items", "properties", "attributes", "parameters",
    "options", "settings", "resources", "elements", "components", "things",
}

NP_NOISE_PREFIXES = re.compile(
    r"^(valid values for|type of|types of|list of|set of|number of|example of|examples of|use of|part of|name of)\s+",
    flags=re.I,
)

LEADING_PREPS = {"of", "in", "to", "for", "by", "on", "at", "from", "with", "about"}
STOP_LAST_WORDS = {"that", "which", "of", "in", "to", "the", "a", "an", "and", "or", "with", "by", "for"}
JUNK_RE = re.compile(r"[=\{\}\(\)<>]|https?://|^\d+$")

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
    "be", "have", "do", "make", "is", "are", "was", "were",
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
    "track", "trigger", "update", "upload", "use", "validate", "verify",
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
    "metric alarm": "CloudWatch metric alarm resource",
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
    "s3", "amazon s3", "simple storage service", "bucket", "buckets",
    "object", "objects", "acl", "acls", "access point", "access points",
    "versioning", "lifecycle", "multipart", "upload", "uploads",
    "replication", "storage class", "storage classes", "checksum",
    "checksums", "glacier", "vault", "vaults", "archive", "archives",
    "outposts",
    "ec2", "amazon ec2", "instance", "instances", "ami", "amis",
    "image", "images", "volume", "volumes", "snapshot", "snapshots",
    "ebs", "elastic block store", "security group", "security groups",
    "key pair", "key pairs", "network interface", "network interfaces",
    "elastic ip", "elastic ips", "placement group", "placement groups",
    "launch template", "launch templates", "auto scaling", "enclave",
    "enclaves",
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
    "iam", "sts", "access analyzer", "roles anywhere", "trust policy",
    "trust policies", "identity policy", "identity policies",
    "resource policy", "resource policies", "managed policy",
    "managed policies", "inline policy", "inline policies", "assume role",
    "federation", "saml", "oidc", "mfa", "access key", "access keys",
    "temporary credentials", "permission set", "service principal",
    "lambda", "aws lambda", "function", "functions", "runtime",
    "runtimes", "handler", "handlers", "layer", "layers", "alias",
    "aliases", "version", "versions", "event source", "event sources",
    "event source mapping", "event source mappings", "trigger",
    "triggers", "concurrency", "provisioned concurrency", "execution role",
    "destination", "destinations", "dead-letter queue", "snapstart",
    "serverless",
    "rds", "amazon rds", "aurora", "database", "databases",
    "db instance", "db instances", "db cluster", "db clusters",
    "db engine", "db engines", "parameter group", "parameter groups",
    "option group", "option groups", "subnet group", "subnet groups",
    "read replica", "read replicas", "backup", "backups",
    "restore", "snapshot", "snapshots", "performance insights",
    "postgresql", "mysql", "mariadb", "oracle", "sql server",
    "rds data api",
    "cloudwatch", "amazon cloudwatch", "cloudwatch logs",
    "log group", "log groups", "log stream", "log streams",
    "metric alarm", "metric alarms", "composite alarm",
    "composite alarms", "dashboard", "dashboards", "namespace",
    "namespaces", "dimension", "dimensions", "eventbridge",
    "event bus", "event buses", "rule", "rules", "target", "targets",
    "synthetics", "canary", "canaries", "rum", "application signals",
    "app insights", "internet monitor", "network flow monitor",
    "observability", "aiops", "trace", "traces",
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

NOISE_PATTERNS_COMPILED = [
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

# ── Sentence-level rejection patterns ──────────────────────────────────────────
SENT_REJECT_HTTP = re.compile(
    r"\b(GET|PUT|POST|DELETE|HEAD|PATCH|OPTIONS)\s+[/\w]|HTTP/\d",
    re.IGNORECASE,
)
SENT_REJECT_TIMESTAMP = re.compile(
    r"\b\d{1,2}\s+\w{3}\s+\d{4}\s+\d{2}:\d{2}:\d{2}|\d{4}-\d{2}-\d{2}T\d{2}:\d{2}",
)
SENT_REJECT_XML = re.compile(r"<\w[\w:]*[\s/>]|</\w[\w:]*>")
SENT_REJECT_PATH = re.compile(r"(?:^|[\s\"'])/[\w./%-]{4,}")
SENT_REJECT_SYMBOLS = re.compile(r"[=<>{}\[\]]{2,}|\?\w+=")
SENT_REJECT_ELLIPSIS = re.compile(r"\.{4,}|_{4,}")
SENT_REJECT_CONTINUATION = re.compile(
    r"^\s*(for example|for instance|see also|note that|the following|as shown|as described|refer to|see the)",
    re.IGNORECASE,
)
SENT_REJECT_PROCEDURAL = re.compile(
    r"^\s*(step\s+\d|click\s+|navigate\s+to\s+|go\s+to\s+the\s+console|open\s+the\s+console|"
    r"in\s+the\s+(aws\s+)?console|from\s+the\s+(left\s+)?navigation|"
    r"to\s+\w+,?\s+(you\s+must\s+first|you\s+need\s+to|scroll|click|select\s+from))",
    re.IGNORECASE,
)

# ── Phrase-level rejection patterns ────────────────────────────────────────────
PHRASE_REJECT_DANGLING_PREP = re.compile(
    r"\b(of|in|to|for|by|on|at|from|with|about|that|which|when|where|whose|if)\s*$",
    re.IGNORECASE,
)
PHRASE_REJECT_DATE_FRAG = re.compile(
    r"\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b|\bGMT\b",
    re.IGNORECASE,
)
PHRASE_REJECT_HTTP_VERB = re.compile(
    r"^(?:GET|PUT|POST|DELETE|HEAD|PATCH|OPTIONS|HTTP)\b",
    re.IGNORECASE,
)
PHRASE_REJECT_SLASH = re.compile(r"/\w+/|^\?|&\w+=")
PHRASE_REJECT_REL_CLAUSE = re.compile(r"\b(that|which|who|whom|whose)\s*$", re.IGNORECASE)
PHRASE_REJECT_AUX_CHAIN = re.compile(
    r"\b(is|are|was|were|be|been|being|have|has|had|will|would|shall|should|may|might|must|can|could)\s+"
    r"(is|are|was|were|be|been|being|have|has|had|will|would|shall|should|may|might|must|can|could)\b",
    re.IGNORECASE,
)

# ── Copula-allowed definitional verbs (only strong definitional copulas kept) ──
COPULA_STRONG_HEADS = {
    "type", "format", "mechanism", "protocol", "standard", "algorithm",
    "identifier", "name", "structure", "class", "category",
}

# ── Confidence scoring weights ─────────────────────────────────────────────────
CONFIDENCE_WEIGHTS = {
    "subject_capitalized": 2,
    "object_capitalized": 2,
    "subject_domain_specific": 3,
    "object_domain_specific": 3,
    "verb_in_good_verbs": 2,
    "subject_multiword": 1,
    "object_multiword": 1,
    "subject_has_camelcase": 2,
    "object_has_camelcase": 2,
    "subject_xamz": 3,
}
CONFIDENCE_THRESHOLD = 3

MAX_AKUS = 8

NARRATIVE_TOKENS = {
    "example", "section", "step", "steps", "following", "above", "below",
    "table", "figure", "diagram", "line", "note", "summary", "overview",
    "process", "procedure", "case", "scenario", "situation", "context",
}

GENERIC_SHORT_SUBJECTS = {
    "system", "service", "function", "data", "value", "object",
    "request", "response", "result", "bucket", "resource", "feature",
    "component", "module", "item", "element", "entity", "operation",
}

NARRATIVE_OBJECT_PHRASES = {
    "following", "example", "steps", "process", "procedure",
    "above", "below", "section", "figure", "table", "diagram",
}


def is_code_noise(text):
    return bool(CODE_RE.search(text))


def is_http_noise(text):
    return bool(HTTP_RE.search(text))


def is_domain_phrase(text):
    return bool(DOMAIN_RE.search(text))


def is_specific_domain_phrase(text):
    return bool(SPECIFIC_DOMAIN_RE.search(text))