
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __gnu_CORBA_OrbFocused__
#define __gnu_CORBA_OrbFocused__

#pragma interface

#include <gnu/CORBA/Poa/ORB_1_4.h>
#include <gcj/array.h>

extern "Java"
{
  namespace gnu
  {
    namespace CORBA
    {
        class IOR;
        class OrbFocused;
        class OrbFunctional$portServer;
    }
  }
  namespace java
  {
    namespace applet
    {
        class Applet;
    }
  }
  namespace org
  {
    namespace omg
    {
      namespace CORBA
      {
          class Object;
      }
    }
  }
}

class gnu::CORBA::OrbFocused : public ::gnu::CORBA::Poa::ORB_1_4
{

public:
  OrbFocused();
  virtual void setPortRange(::java::lang::String *);
  virtual void setPortRange(jint, jint);
public: // actually package-private
  virtual jint getPortFromRange(jint);
public: // actually protected
  virtual ::gnu::CORBA::OrbFunctional$portServer * getPortServer(jint);
public:
  virtual void run();
  virtual jint getFreePort();
  virtual void connect_1_thread(::org::omg::CORBA::Object *, JArray< jbyte > *, ::java::lang::Object *);
  virtual void startService(::gnu::CORBA::IOR *);
public: // actually protected
  virtual void set_parameters(::java::applet::Applet *, ::java::util::Properties *);
  virtual void set_parameters(JArray< ::java::lang::String * > *, ::java::util::Properties *);
  virtual void useProperties(::java::util::Properties *);
public:
  static ::java::lang::String * LISTENER_PORT;
public: // actually package-private
  jint __attribute__((aligned(__alignof__( ::gnu::CORBA::Poa::ORB_1_4)))) m_ports_from;
  jint m_ports_to;
  static const jint PARALLEL = 0;
  static const jint SEQUENTIAL = 1;
  ::java::util::Random * m_random;
public:
  static ::java::lang::Class class$;
};

#endif // __gnu_CORBA_OrbFocused__
