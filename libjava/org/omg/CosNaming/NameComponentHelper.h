
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __org_omg_CosNaming_NameComponentHelper__
#define __org_omg_CosNaming_NameComponentHelper__

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
        namespace portable
        {
            class InputStream;
            class OutputStream;
        }
      }
      namespace CosNaming
      {
          class NameComponent;
          class NameComponentHelper;
      }
    }
  }
}

class org::omg::CosNaming::NameComponentHelper : public ::java::lang::Object
{

public:
  NameComponentHelper();
  static ::org::omg::CosNaming::NameComponent * extract(::org::omg::CORBA::Any *);
  static ::java::lang::String * id();
  static void insert(::org::omg::CORBA::Any *, ::org::omg::CosNaming::NameComponent *);
  static ::org::omg::CosNaming::NameComponent * read(::org::omg::CORBA::portable::InputStream *);
  static ::org::omg::CORBA::TypeCode * type();
  static void write(::org::omg::CORBA::portable::OutputStream *, ::org::omg::CosNaming::NameComponent *);
private:
  static ::java::lang::String * _id;
public:
  static ::java::lang::Class class$;
};

#endif // __org_omg_CosNaming_NameComponentHelper__
