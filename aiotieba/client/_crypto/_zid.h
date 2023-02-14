#pragma once

#define TBC_CBC_SECKEY_SIZE 16
#define TBC_RC4_SIZE 16

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief RC4 includes an extra XOR against 42
 *
 * @param dst 16 bytes. alloc and free by user
 * @param xyusMd5Str 32 bytes. alloc and free by user
 * @param cbcSecKey 16 bytes. alloc and free by user
 *
 * @return non 0 if any error
 *
 * @note 12.x loc: com.baidu.sofire.x6.oCOCcooCCoC.ocOOCCoOOCcC.CcooOoocOOo
 */
int tbc_rc4_42(char *dst, const char *xyusMd5Str, const char *cbcSecKey);

#ifdef __cplusplus
}
#endif