
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ASIGNACION BOOLEANO DECIMAL ENTERO EQ FCIENT GE GT ID LE LT NOTCIENT OCTAL SALTO SEPARADOR SIMBOLO VARTYPE V_BOOLEANsentencias : statement SALTO sentencias\n        | statement statement : VARTYPE declarationstatement : VARTYPE ID '=' expressionSRstatement : ID '=' expressionSR\n                | ID '=' booleanstatement : expressionSR\n                    | booleanboolean : expressionLOGboolean :  expressionLOG BOOLEANO booleandeclaration : identificador\n                    |  identificador ',' declaration identificador : IDexpressionLOG : expressionSR LT expressionSR\n                        | expressionSR GT expressionSR\n                        | expressionSR LE expressionSR\n                        | expressionSR GE expressionSR\n                        | expressionSR EQ expressionSRstatement : \nexpressionSR : expressionSR '+' expressionMD\n                  | expressionSR '-' expressionMDexpressionSR : expressionMDexpressionMD : expressionMD '*' expression\n                  | expressionMD '/' expressionexpressionMD : expressionexpression : '(' expressionSR ')'expression : '-' expression\n                | '+' expression\n                expression : ENTERO\n                | DECIMAL\n                | V_BOOLEAN\n                | NOTCIENT\n                | OCTAL\n    expression : FCIENT '(' expressionSR ')'expression : ID "
    
_lr_action_items = {'VARTYPE':([0,19,],[3,3,]),'ID':([0,3,7,9,12,19,23,24,25,26,27,28,29,30,33,34,36,38,40,41,],[4,21,32,32,32,4,32,32,32,32,32,32,32,32,32,32,32,32,32,59,]),'SALTO':([0,2,4,5,6,8,10,11,13,14,15,16,17,19,20,21,22,31,32,35,42,43,44,45,46,47,48,49,50,51,52,53,55,57,58,59,60,],[-19,19,-35,-7,-8,-22,-9,-25,-29,-30,-31,-32,-33,-19,-3,-13,-11,-28,-35,-27,-5,-6,-20,-21,-14,-15,-16,-17,-18,-23,-24,-10,-26,-4,-12,-13,-34,]),'$end':([0,1,2,4,5,6,8,10,11,13,14,15,16,17,19,20,21,22,31,32,35,39,42,43,44,45,46,47,48,49,50,51,52,53,55,57,58,59,60,],[-19,0,-2,-35,-7,-8,-22,-9,-25,-29,-30,-31,-32,-33,-19,-3,-13,-11,-28,-35,-27,-1,-5,-6,-20,-21,-14,-15,-16,-17,-18,-23,-24,-10,-26,-4,-12,-13,-34,]),'(':([0,7,9,12,18,19,23,24,25,26,27,28,29,30,33,34,36,38,40,],[12,12,12,12,38,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'-':([0,4,5,7,8,9,11,12,13,14,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,42,44,45,46,47,48,49,50,51,52,54,55,56,57,60,],[9,-35,25,9,-22,9,-25,9,-29,-30,-31,-32,-33,9,9,9,9,9,9,9,9,9,-28,-35,9,9,-27,9,25,9,9,25,-20,-21,25,25,25,25,25,-23,-24,25,-26,25,25,-34,]),'+':([0,4,5,7,8,9,11,12,13,14,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,42,44,45,46,47,48,49,50,51,52,54,55,56,57,60,],[7,-35,24,7,-22,7,-25,7,-29,-30,-31,-32,-33,7,7,7,7,7,7,7,7,7,-28,-35,7,7,-27,7,24,7,7,24,-20,-21,24,24,24,24,24,-23,-24,24,-26,24,24,-34,]),'ENTERO':([0,7,9,12,19,23,24,25,26,27,28,29,30,33,34,36,38,40,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'DECIMAL':([0,7,9,12,19,23,24,25,26,27,28,29,30,33,34,36,38,40,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'V_BOOLEAN':([0,7,9,12,19,23,24,25,26,27,28,29,30,33,34,36,38,40,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'NOTCIENT':([0,7,9,12,19,23,24,25,26,27,28,29,30,33,34,36,38,40,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'OCTAL':([0,7,9,12,19,23,24,25,26,27,28,29,30,33,34,36,38,40,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'FCIENT':([0,7,9,12,19,23,24,25,26,27,28,29,30,33,34,36,38,40,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'=':([4,21,],[23,40,]),'*':([4,8,11,13,14,15,16,17,31,32,35,44,45,51,52,55,60,],[-35,33,-25,-29,-30,-31,-32,-33,-28,-35,-27,33,33,-23,-24,-26,-34,]),'/':([4,8,11,13,14,15,16,17,31,32,35,44,45,51,52,55,60,],[-35,34,-25,-29,-30,-31,-32,-33,-28,-35,-27,34,34,-23,-24,-26,-34,]),'LT':([4,5,8,11,13,14,15,16,17,31,32,35,42,44,45,51,52,54,55,60,],[-35,26,-22,-25,-29,-30,-31,-32,-33,-28,-35,-27,26,-20,-21,-23,-24,26,-26,-34,]),'GT':([4,5,8,11,13,14,15,16,17,31,32,35,42,44,45,51,52,54,55,60,],[-35,27,-22,-25,-29,-30,-31,-32,-33,-28,-35,-27,27,-20,-21,-23,-24,27,-26,-34,]),'LE':([4,5,8,11,13,14,15,16,17,31,32,35,42,44,45,51,52,54,55,60,],[-35,28,-22,-25,-29,-30,-31,-32,-33,-28,-35,-27,28,-20,-21,-23,-24,28,-26,-34,]),'GE':([4,5,8,11,13,14,15,16,17,31,32,35,42,44,45,51,52,54,55,60,],[-35,29,-22,-25,-29,-30,-31,-32,-33,-28,-35,-27,29,-20,-21,-23,-24,29,-26,-34,]),'EQ':([4,5,8,11,13,14,15,16,17,31,32,35,42,44,45,51,52,54,55,60,],[-35,30,-22,-25,-29,-30,-31,-32,-33,-28,-35,-27,30,-20,-21,-23,-24,30,-26,-34,]),')':([8,11,13,14,15,16,17,31,32,35,37,44,45,51,52,55,56,60,],[-22,-25,-29,-30,-31,-32,-33,-28,-35,-27,55,-20,-21,-23,-24,-26,60,-34,]),'BOOLEANO':([8,10,11,13,14,15,16,17,31,32,35,44,45,46,47,48,49,50,51,52,55,60,],[-22,36,-25,-29,-30,-31,-32,-33,-28,-35,-27,-20,-21,-14,-15,-16,-17,-18,-23,-24,-26,-34,]),',':([21,22,59,],[-13,41,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,19,],[1,39,]),'statement':([0,19,],[2,2,]),'expressionSR':([0,12,19,23,26,27,28,29,30,36,38,40,],[5,37,5,42,46,47,48,49,50,54,56,57,]),'boolean':([0,19,23,36,],[6,6,43,53,]),'expressionMD':([0,12,19,23,24,25,26,27,28,29,30,36,38,40,],[8,8,8,8,44,45,8,8,8,8,8,8,8,8,]),'expressionLOG':([0,19,23,36,],[10,10,10,10,]),'expression':([0,7,9,12,19,23,24,25,26,27,28,29,30,33,34,36,38,40,],[11,31,35,11,11,11,11,11,11,11,11,11,11,51,52,11,11,11,]),'declaration':([3,41,],[20,58,]),'identificador':([3,41,],[22,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> statement SALTO sentencias','sentencias',3,'p_statement_sl_statement','calc.py',209),
  ('sentencias -> statement','sentencias',1,'p_statement_sl_statement','calc.py',210),
  ('statement -> VARTYPE declaration','statement',2,'p_statement_declaration','calc.py',213),
  ('statement -> VARTYPE ID = expressionSR','statement',4,'p_statement_dec_assign','calc.py',250),
  ('statement -> ID = expressionSR','statement',3,'p_statement_assign','calc.py',258),
  ('statement -> ID = boolean','statement',3,'p_statement_assign','calc.py',259),
  ('statement -> expressionSR','statement',1,'p_statement_expr','calc.py',269),
  ('statement -> boolean','statement',1,'p_statement_expr','calc.py',270),
  ('boolean -> expressionLOG','boolean',1,'p_boolean_single','calc.py',274),
  ('boolean -> expressionLOG BOOLEANO boolean','boolean',3,'p_statement_boolean','calc.py',278),
  ('declaration -> identificador','declaration',1,'p_declaracion_variables','calc.py',298),
  ('declaration -> identificador , declaration','declaration',3,'p_declaracion_variables','calc.py',299),
  ('identificador -> ID','identificador',1,'p_statement_declarationSimple','calc.py',313),
  ('expressionLOG -> expressionSR LT expressionSR','expressionLOG',3,'p_expressionLOG','calc.py',323),
  ('expressionLOG -> expressionSR GT expressionSR','expressionLOG',3,'p_expressionLOG','calc.py',324),
  ('expressionLOG -> expressionSR LE expressionSR','expressionLOG',3,'p_expressionLOG','calc.py',325),
  ('expressionLOG -> expressionSR GE expressionSR','expressionLOG',3,'p_expressionLOG','calc.py',326),
  ('expressionLOG -> expressionSR EQ expressionSR','expressionLOG',3,'p_expressionLOG','calc.py',327),
  ('statement -> <empty>','statement',0,'p_statement_sl','calc.py',356),
  ('expressionSR -> expressionSR + expressionMD','expressionSR',3,'p_expression_binop','calc.py',359),
  ('expressionSR -> expressionSR - expressionMD','expressionSR',3,'p_expression_binop','calc.py',360),
  ('expressionSR -> expressionMD','expressionSR',1,'p_expressionSR_expressionMD','calc.py',367),
  ('expressionMD -> expressionMD * expression','expressionMD',3,'p_expression_opmd','calc.py',372),
  ('expressionMD -> expressionMD / expression','expressionMD',3,'p_expression_opmd','calc.py',373),
  ('expressionMD -> expression','expressionMD',1,'p_expressionMD_expression','calc.py',380),
  ('expression -> ( expressionSR )','expression',3,'p_expression_group','calc.py',386),
  ('expression -> - expression','expression',2,'p_expression_signo','calc.py',391),
  ('expression -> + expression','expression',2,'p_expression_signo','calc.py',392),
  ('expression -> ENTERO','expression',1,'p_expression_basica','calc.py',401),
  ('expression -> DECIMAL','expression',1,'p_expression_basica','calc.py',402),
  ('expression -> V_BOOLEAN','expression',1,'p_expression_basica','calc.py',403),
  ('expression -> NOTCIENT','expression',1,'p_expression_basica','calc.py',404),
  ('expression -> OCTAL','expression',1,'p_expression_basica','calc.py',405),
  ('expression -> FCIENT ( expressionSR )','expression',4,'p_expression_fcient','calc.py',410),
  ('expression -> ID','expression',1,'p_expression_name','calc.py',422),
]
