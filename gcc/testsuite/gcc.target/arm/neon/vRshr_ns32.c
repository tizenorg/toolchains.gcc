/* Test the `vRshr_ns32' ARM Neon intrinsic.  */
/* This file was autogenerated by neon-testgen.  */

/* { dg-do assemble } */
/* { dg-require-effective-target arm_neon_ok } */
/* { dg-options "-save-temps -O0 -mfpu=neon -mfloat-abi=softfp" } */

#include "arm_neon.h"

void test_vRshr_ns32 (void)
{
  int32x2_t out_int32x2_t;
  int32x2_t arg0_int32x2_t;

  out_int32x2_t = vrshr_n_s32 (arg0_int32x2_t, 1);
}

/* { dg-final { scan-assembler "vrshr\.s32\[ 	\]+\[dD\]\[0-9\]+, \[dD\]\[0-9\]+, #\[0-9\]+!?\(\[ 	\]+@\[a-zA-Z0-9 \]+\)?\n" } } */
/* { dg-final { cleanup-saved-temps } } */
