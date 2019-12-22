from os import environ
from __core__.utilities import decode_base64_to_json

AVAILABLE_FILE_TYPES = [
    'abap', 'abc', 'actionscript', 'ada', 'apache_conf', 'apex', 'applescript', 'asciidoc', 'asl',
    'assembly_x86', 'autohotkey', 'batchfile', 'bro', 'c9search', 'c_cpp', 'cirru', 'clojure', 'cobol',
    'coffee', 'coldfusion', 'csharp', 'csound_document', 'csound_orchestra', 'csound_score', 'csp', 'css',
    'curly', 'd', 'dart', 'diff', 'django', 'dockerfile', 'dot', 'drools', 'edifact', 'eiffel', 'ejs',
    'elixir', 'elm', 'erlang', 'forth', 'fortran', 'fsharp', 'fsl', 'ftl', 'gcode', 'gherkin', 'gitignore',
    'glsl', 'gobstones', 'golang', 'graphqlschema', 'groovy', 'haml', 'handlebars', 'haskell',
    'haskell_cabal', 'haxe', 'hjson', 'html', 'html_elixir', 'html_ruby', 'ini', 'io', 'jack', 'jade', 'java',
    'javascript', 'json', 'jsoniq', 'jsp', 'jssm', 'jsx', 'julia', 'kotlin', 'latex', 'less', 'liquid',
    'lisp', 'livescript', 'logiql', 'logtalk', 'lsl', 'lua', 'luapage', 'lucene', 'makefile', 'markdown',
    'mask', 'matlab', 'maze', 'mel', 'mixal', 'mushcode', 'mysql', 'nix', 'nsis', 'objectivec', 'ocaml',
    'pascal', 'perl', 'perl6', 'pgsql', 'php', 'php_laravel_blade', 'pig', 'plain_text', 'powershell',
    'praat', 'prolog', 'properties', 'protobuf', 'puppet', 'python', 'r', 'razor', 'rdoc', 'red', 'redshift',
    'rhtml', 'rst', 'ruby', 'rust', 'sass', 'scad', 'scala', 'scheme', 'scss', 'sh', 'sjs', 'slim', 'smarty',
    'snippets', 'soy_template', 'space', 'sparql', 'sql', 'sqlserver', 'stylus', 'svg', 'swift', 'tcl',
    'terraform', 'tex', 'text', 'textile', 'toml', 'tsx', 'turtle', 'twig', 'typescript', 'vala', 'vbscript',
    'velocity', 'verilog', 'vhdl', 'visualforce', 'wollok', 'xml', 'xquery', 'yaml'
]
SHEET_DATA_S3_BUCKET=environ['SHEET_DATA_S3_BUCKET']
ADMIN_USER_GROUP='admin'
PUBLIC_SHEETS_FOLDER='public'
COGNITO_JWKS_BASE64=environ['COGNITO_JWKS_BASE64']
COGNITO_CLIENT_ID=environ['COGNITO_CLIENT_ID']
