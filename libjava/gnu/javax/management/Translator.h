
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __gnu_javax_management_Translator__
#define __gnu_javax_management_Translator__

#pragma interface

#include <java/lang/Object.h>
#include <gcj/array.h>

extern "Java"
{
  namespace gnu
  {
    namespace javax
    {
      namespace management
      {
          class Translator;
      }
    }
  }
  namespace javax
  {
    namespace management
    {
      namespace openmbean
      {
          class OpenMBeanParameterInfo;
          class OpenType;
      }
    }
  }
}

class gnu::javax::management::Translator : public ::java::lang::Object
{

public:
  Translator();
  static JArray< ::java::lang::Object * > * fromJava(JArray< ::java::lang::Object * > *, ::java::lang::reflect::Method *);
  static ::java::lang::Object * fromJava(::java::lang::Object *, ::java::lang::reflect::Type *);
  static ::java::lang::Object * toJava(::java::lang::Object *, ::java::lang::reflect::Method *);
private:
  static JArray< ::java::lang::Object * > * makeArraySpecific(JArray< ::java::lang::Object * > *);
public:
  static ::javax::management::openmbean::OpenMBeanParameterInfo * translate(::java::lang::String *);
private:
  static ::javax::management::openmbean::OpenType * getTypeFromClass(::java::lang::Class *);
  static ::java::lang::String * getTypeName(::java::lang::reflect::Type *);
public:
  static ::java::lang::Class class$;
};

#endif // __gnu_javax_management_Translator__
