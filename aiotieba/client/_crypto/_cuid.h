#pragma once

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief impl of TiebaLite tieba/post/utils/helios
 *
 * @param dst 5 bytes. alloc and free by user
 * @param src alloc and free by user
 * @param srcSize size of src. must >= 1
 *
 * @return non 0 if any error
 *
 * @note 12.x loc: com.baidu.tieba.l40.a / com.baidu.tieba.pz.a
 */
int tbc_heliosHash(char *dst, const char *src, size_t srcSize);

/**
 * @brief generate `cuid_galaxy2`
 *
 * @param dst 42 bytes. alloc and free by user
 * @param androidID 16 bytes. alloc and free by user
 *
 * @return non 0 if any error
 *
 * @note 12.x loc: com.baidu.tieba.oz.m
 */
int tbc_cuid_galaxy2(char *dst, const char *androidID);

/**
 * @brief generate `c3_aid`
 *
 * @param dst 45 bytes. alloc and free by user
 * @param androidID 16 bytes. alloc and free by user
 * @param uuid 36 bytes. alloc and free by user
 *
 * @return non 0 if any error
 *
 * @note 12.x loc: com.baidu.tieba.r50.f
 */
int tbc_c3_aid(char *dst, const char *androidID, const char *uuid);

#ifdef __cplusplus
}
#endif
