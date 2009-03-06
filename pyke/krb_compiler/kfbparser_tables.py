
# /home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser_tables.py
# This file is automatically generated. Do not edit.
_tabversion = '3.0'

_lr_method = 'LALR'

_lr_signature = -12646522
    
_lr_action_items = {'NONE_TOK':([7,9,20,23,],[8,8,8,8,]),'LP_TOK':([5,7,9,20,23,],[7,9,9,9,9,]),'STRING_TOK':([7,9,20,23,],[10,10,10,10,]),'RP_TOK':([7,8,9,10,11,12,13,14,15,17,18,19,23,24,25,27,],[16,-6,18,-12,-11,21,-14,-15,-13,-17,-16,-7,-8,27,-18,-19,]),',':([8,10,11,12,13,14,15,17,18,19,25,27,],[-6,-12,-11,20,-14,-15,-13,-17,-16,23,-18,-19,]),'NUMBER_TOK':([7,9,20,23,],[11,11,11,11,]),'NL_TOK':([0,16,21,],[3,22,26,]),'TRUE_TOK':([7,9,20,23,],[14,14,14,14,]),'IDENTIFIER_TOK':([0,1,3,4,6,7,9,20,22,23,26,],[-9,-2,-10,5,-3,15,15,15,-4,15,-5,]),'FALSE_TOK':([7,9,20,23,],[13,13,13,13,]),'$end':([0,1,2,3,4,6,22,26,],[-9,-2,0,-10,-1,-3,-4,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'nl_opt':([0,],[1,]),'comma_opt':([19,],[24,]),'data_list':([7,9,],[12,19,]),'file':([0,],[2,]),'facts':([1,],[4,]),'data':([7,9,20,23,],[17,17,25,25,]),'fact':([4,],[6,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> file","S'",1,None,None,None),
  ('file -> nl_opt facts','file',2,'p_file','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',36),
  ('facts -> <empty>','facts',0,'p_file','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',37),
  ('facts -> facts fact','facts',2,'p_file','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',38),
  ('fact -> IDENTIFIER_TOK LP_TOK RP_TOK NL_TOK','fact',4,'p_fact0','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',43),
  ('fact -> IDENTIFIER_TOK LP_TOK data_list RP_TOK NL_TOK','fact',5,'p_fact1','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',47),
  ('data -> NONE_TOK','data',1,'p_none','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',51),
  ('comma_opt -> <empty>','comma_opt',0,'p_none','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',52),
  ('comma_opt -> ,','comma_opt',1,'p_none','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',53),
  ('nl_opt -> <empty>','nl_opt',0,'p_none','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',54),
  ('nl_opt -> NL_TOK','nl_opt',1,'p_none','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',55),
  ('data -> NUMBER_TOK','data',1,'p_number','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',60),
  ('data -> STRING_TOK','data',1,'p_string','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',65),
  ('data -> IDENTIFIER_TOK','data',1,'p_quoted_last','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',70),
  ('data -> FALSE_TOK','data',1,'p_false','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',75),
  ('data -> TRUE_TOK','data',1,'p_true','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',80),
  ('data -> LP_TOK RP_TOK','data',2,'p_empty_tuple','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',85),
  ('data_list -> data','data_list',1,'p_start_list','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',90),
  ('data_list -> data_list , data','data_list',3,'p_append_list','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',95),
  ('data -> LP_TOK data_list comma_opt RP_TOK','data',4,'p_tuple','/home/bruce/python/workareas/sf.trunk/pyke/krb_compiler/kfbparser.py',101),
]
