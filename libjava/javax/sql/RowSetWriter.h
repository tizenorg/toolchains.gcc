
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __javax_sql_RowSetWriter__
#define __javax_sql_RowSetWriter__

#pragma interface

#include <java/lang/Object.h>
extern "Java"
{
  namespace javax
  {
    namespace sql
    {
        class RowSetInternal;
        class RowSetWriter;
    }
  }
}

class javax::sql::RowSetWriter : public ::java::lang::Object
{

public:
  virtual jboolean writeData(::javax::sql::RowSetInternal *) = 0;
  static ::java::lang::Class class$;
} __attribute__ ((java_interface));

#endif // __javax_sql_RowSetWriter__
