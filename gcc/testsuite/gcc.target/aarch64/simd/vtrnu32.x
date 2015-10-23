extern void abort (void);

uint32x2x2_t
test_vtrnu32 (uint32x2_t _a, uint32x2_t _b)
{
  return vtrn_u32 (_a, _b);
}

int
main (int argc, char **argv)
{
  int i;
  uint32_t first[] = {1, 2};
  uint32_t second[] = {3, 4};
  uint32x2x2_t result = test_vtrnu32 (vld1_u32 (first), vld1_u32 (second));
  uint32x2_t res1 = result.val[0], res2 = result.val[1];
  uint32_t exp1[] = {1, 3};
  uint32_t exp2[] = {2, 4};
  uint32x2_t expected1 = vld1_u32 (exp1);
  uint32x2_t expected2 = vld1_u32 (exp2);

  for (i = 0; i < 2; i++)
    if ((res1[i] != expected1[i]) || (res2[i] != expected2[i]))
      abort ();

  return 0;
}
