
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __org_omg_DynamicAny_DynAnyFactoryOperations__
#define __org_omg_DynamicAny_DynAnyFactoryOperations__

#pragma interface

#include <java/lang/Object.h>
extern "Java"
{
  namespace org
  {
    namespace omg
    {
      namespace CORBA
      {
          class Any;
          class TypeCode;
      }
      namespace DynamicAny
      {
          class DynAny;
          class DynAnyFactoryOperations;
      }
    }
  }
}

class org::omg::DynamicAny::DynAnyFactoryOperations : public ::java::lang::Object
{

public:
  virtual ::org::omg::DynamicAny::DynAny * create_dyn_any_from_type_code(::org::omg::CORBA::TypeCode *) = 0;
  virtual ::org::omg::DynamicAny::DynAny * create_dyn_any(::org::omg::CORBA::Any *) = 0;
  static ::java::lang::Class class$;
} __attribute__ ((java_interface));

#endif // __org_omg_DynamicAny_DynAnyFactoryOperations__
