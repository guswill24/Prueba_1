// JSON.g4
grammar JSON;

json : jsonObject | array ;

jsonObject
    : '{' pair (',' pair)* '}'   # AnObject
    | '{' '}'                    # EmptyObject
    ;

pair : STRING ':' value ;

array
    : '[' value (',' value)* ']' # ArrayOfValues
    | '[' ']'                    # EmptyArray
    ;

value
    : STRING       # String
    | NUMBER       # Atom
    | jsonObject   # ObjectValue
    | array        # ArrayValue
    | 'true'       # Atom
    | 'false'      # Atom
    | 'null'       # Atom
    ;

STRING : '"' ('\\' . | ~ ["\\])* '"' ;
NUMBER : '-'? INT ('.' [0-9]+)? EXP? ;
fragment INT : '0' | [1-9] [0-9]* ;
fragment EXP : [Ee] [+\-]? INT ;

WS : [ \t\n\r]+ -> skip ;
