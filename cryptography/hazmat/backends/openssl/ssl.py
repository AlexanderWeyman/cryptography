# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

INCLUDES = """
#include <openssl/ssl.h>
"""

TYPES = """
/* Internally invented symbol to tell us if SSLv2 is supported */
static const int Cryptography_HAS_SSL2;

/* Internally invented symbol to tell us if SNI is supported */
static const int Cryptography_HAS_TLSEXT_HOSTNAME;

static const int SSL_FILETYPE_PEM;
static const int SSL_FILETYPE_ASN1;
static const int SSL_ERROR_NONE;
static const int SSL_ERROR_ZERO_RETURN;
static const int SSL_ERROR_WANT_READ;
static const int SSL_ERROR_WANT_WRITE;
static const int SSL_ERROR_WANT_X509_LOOKUP;
static const int SSL_ERROR_SYSCALL;
static const int SSL_ERROR_SSL;
static const int SSL_SENT_SHUTDOWN;
static const int SSL_RECEIVED_SHUTDOWN;
static const int SSL_OP_NO_SSLv2;
static const int SSL_OP_NO_SSLv3;
static const int SSL_OP_NO_TLSv1;
static const int SSL_OP_SINGLE_DH_USE;
static const int SSL_OP_EPHEMERAL_RSA;
static const int SSL_OP_MICROSOFT_SESS_ID_BUG;
static const int SSL_OP_NETSCAPE_CHALLENGE_BUG;
static const int SSL_OP_NETSCAPE_REUSE_CIPHER_CHANGE_BUG;
static const int SSL_OP_SSLREF2_REUSE_CERT_TYPE_BUG;
static const int SSL_OP_MICROSOFT_BIG_SSLV3_BUFFER;
static const int SSL_OP_MSIE_SSLV2_RSA_PADDING;
static const int SSL_OP_SSLEAY_080_CLIENT_DH_BUG;
static const int SSL_OP_TLS_D5_BUG;
static const int SSL_OP_TLS_BLOCK_PADDING_BUG;
static const int SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS;
static const int SSL_OP_CIPHER_SERVER_PREFERENCE;
static const int SSL_OP_TLS_ROLLBACK_BUG;
static const int SSL_OP_PKCS1_CHECK_1;
static const int SSL_OP_PKCS1_CHECK_2;
static const int SSL_OP_NETSCAPE_CA_DN_BUG;
static const int SSL_OP_NETSCAPE_DEMO_CIPHER_CHANGE_BUG;
static const int SSL_OP_NO_QUERY_MTU;
static const int SSL_OP_COOKIE_EXCHANGE;
static const int SSL_OP_NO_TICKET;
static const int SSL_OP_ALL;
static const int SSL_VERIFY_PEER;
static const int SSL_VERIFY_FAIL_IF_NO_PEER_CERT;
static const int SSL_VERIFY_CLIENT_ONCE;
static const int SSL_VERIFY_NONE;
static const int SSL_SESS_CACHE_OFF;
static const int SSL_SESS_CACHE_CLIENT;
static const int SSL_SESS_CACHE_SERVER;
static const int SSL_SESS_CACHE_BOTH;
static const int SSL_SESS_CACHE_NO_AUTO_CLEAR;
static const int SSL_SESS_CACHE_NO_INTERNAL_LOOKUP;
static const int SSL_SESS_CACHE_NO_INTERNAL_STORE;
static const int SSL_SESS_CACHE_NO_INTERNAL;
static const int SSL_ST_CONNECT;
static const int SSL_ST_ACCEPT;
static const int SSL_ST_MASK;
static const int SSL_ST_INIT;
static const int SSL_ST_BEFORE;
static const int SSL_ST_OK;
static const int SSL_ST_RENEGOTIATE;
static const int SSL_CB_LOOP;
static const int SSL_CB_EXIT;
static const int SSL_CB_READ;
static const int SSL_CB_WRITE;
static const int SSL_CB_ALERT;
static const int SSL_CB_READ_ALERT;
static const int SSL_CB_WRITE_ALERT;
static const int SSL_CB_ACCEPT_LOOP;
static const int SSL_CB_ACCEPT_EXIT;
static const int SSL_CB_CONNECT_LOOP;
static const int SSL_CB_CONNECT_EXIT;
static const int SSL_CB_HANDSHAKE_START;
static const int SSL_CB_HANDSHAKE_DONE;
static const int SSL_MODE_ENABLE_PARTIAL_WRITE;
static const int SSL_MODE_ACCEPT_MOVING_WRITE_BUFFER;
static const int SSL_MODE_AUTO_RETRY;
static const int SSL3_RANDOM_SIZE;
typedef ... X509_STORE_CTX;
static const int X509_V_OK;
typedef ... SSL_METHOD;
typedef ... SSL_CTX;

typedef struct {
    int master_key_length;
    unsigned char master_key[...];
    ...;
} SSL_SESSION;

typedef struct {
    unsigned char server_random[...];
    unsigned char client_random[...];
    ...;
} SSL3_STATE;

typedef struct {
    SSL3_STATE *s3;
    SSL_SESSION *session;
    ...;
} SSL;

static const int TLSEXT_NAMETYPE_host_name;
"""

FUNCTIONS = """
void SSL_load_error_strings();
int SSL_library_init();

/*  SSL */
SSL_CTX *SSL_set_SSL_CTX(SSL *, SSL_CTX *);
SSL_SESSION *SSL_get1_session(SSL *);
int SSL_set_session(SSL *, SSL_SESSION *);
int SSL_get_verify_mode(const SSL *);
void SSL_set_verify_depth(SSL *, int);
int SSL_get_verify_depth(const SSL *);
int (*SSL_get_verify_callback(const SSL *))(int, X509_STORE_CTX *);
void SSL_set_info_callback(SSL *, void (*)());
void (*SSL_get_info_callback(const SSL *))();
SSL *SSL_new(SSL_CTX *);
void SSL_free(SSL *);
int SSL_set_fd(SSL *, int);
void SSL_set_bio(SSL *, BIO *, BIO *);
void SSL_set_connect_state(SSL *);
void SSL_set_accept_state(SSL *);
void SSL_set_shutdown(SSL *, int);
int SSL_get_shutdown(const SSL *);
int SSL_pending(const SSL *);
int SSL_write(SSL *, const void *, int);
int SSL_read(SSL *, void *, int);
X509 *SSL_get_peer_certificate(const SSL *);
int SSL_get_error(const SSL *, int);
int SSL_do_handshake(SSL *);
int SSL_shutdown(SSL *);
const char *SSL_get_cipher_list(const SSL *, int);

/*  context */
void SSL_CTX_free(SSL_CTX *);
long SSL_CTX_set_timeout(SSL_CTX *, long);
int SSL_CTX_set_default_verify_paths(SSL_CTX *);
void SSL_CTX_set_verify(SSL_CTX *, int, int (*)(int, X509_STORE_CTX *));
void SSL_CTX_set_verify_depth(SSL_CTX *, int);
int (*SSL_CTX_get_verify_callback(const SSL_CTX *))(int, X509_STORE_CTX *);
void SSL_CTX_set_info_callback(SSL_CTX *, void (*)(const SSL *, int, int));
void (*SSL_CTX_get_info_callback(SSL_CTX *))(const SSL *, int, int);
int SSL_CTX_get_verify_mode(const SSL_CTX *);
int SSL_CTX_get_verify_depth(const SSL_CTX *);
int SSL_CTX_set_cipher_list(SSL_CTX *, const char *);
int SSL_CTX_load_verify_locations(SSL_CTX *, const char *, const char *);
void SSL_CTX_set_default_passwd_cb(SSL_CTX *, pem_password_cb *);
void SSL_CTX_set_default_passwd_cb_userdata(SSL_CTX *, void *);
int SSL_CTX_use_certificate(SSL_CTX *, X509 *);
int SSL_CTX_use_certificate_file(SSL_CTX *, const char *, int);
int SSL_CTX_use_certificate_chain_file(SSL_CTX *, const char *);
int SSL_CTX_use_PrivateKey(SSL_CTX *, EVP_PKEY *);
int SSL_CTX_use_PrivateKey_file(SSL_CTX *, const char *, int);
void SSL_CTX_set_cert_store(SSL_CTX *, X509_STORE *);
X509_STORE *SSL_CTX_get_cert_store(const SSL_CTX *);
int SSL_CTX_add_client_CA(SSL_CTX *, X509 *);

/*  X509_STORE_CTX */
int X509_STORE_CTX_get_error(X509_STORE_CTX *);
void X509_STORE_CTX_set_error(X509_STORE_CTX *, int);
int X509_STORE_CTX_get_error_depth(X509_STORE_CTX *);
X509 *X509_STORE_CTX_get_current_cert(X509_STORE_CTX *);

/*  SSL_SESSION */
void SSL_SESSION_free(SSL_SESSION *);
"""

MACROS = """
long SSL_set_mode(SSL *, long);
long SSL_get_mode(SSL *);

long SSL_set_options(SSL *, long);
long SSL_get_options(SSL *);

int SSL_want_read(const SSL *);
int SSL_want_write(const SSL *);

int SSL_total_renegotiations(const SSL *);

long SSL_CTX_set_options(SSL_CTX *, long);
long SSL_CTX_get_options(SSL_CTX *);
long SSL_CTX_set_mode(SSL_CTX *, long);
long SSL_CTX_get_mode(SSL_CTX *);
long SSL_CTX_set_session_cache_mode(SSL_CTX *, long);
long SSL_CTX_get_session_cache_mode(SSL_CTX *);
long SSL_CTX_set_tmp_dh(SSL_CTX *, DH *);
long SSL_CTX_add_extra_chain_cert(SSL_CTX *, X509 *);

/*- These aren't macros these functions are all const X on openssl > 1.0.x -*/

/* SSLv2 support is compiled out of some versions of OpenSSL.  These will
 * get special support when we generate the bindings so that if they are
 * available they will be wrapped, but if they are not they won't cause
 * problems (like link errors).
 */
const SSL_METHOD *SSLv2_method();
const SSL_METHOD *SSLv2_server_method();
const SSL_METHOD *SSLv2_client_method();

/*  methods */
const SSL_METHOD *SSLv3_method();
const SSL_METHOD *SSLv3_server_method();
const SSL_METHOD *SSLv3_client_method();
const SSL_METHOD *TLSv1_method();
const SSL_METHOD *TLSv1_server_method();
const SSL_METHOD *TLSv1_client_method();
const SSL_METHOD *SSLv23_method();
const SSL_METHOD *SSLv23_server_method();
const SSL_METHOD *SSLv23_client_method();

/*- These aren't macros these arguments are all const X on openssl > 1.0.x -*/
SSL_CTX *SSL_CTX_new(const SSL_METHOD *);
long SSL_CTX_get_timeout(const SSL_CTX *);

/* SNI APIs were introduced in OpenSSL 1.0.0.  To continue to support
 * earlier versions some special handling of these is necessary.
 */
void SSL_set_tlsext_host_name(SSL *, char *);
void SSL_CTX_set_tlsext_servername_callback(
    SSL_CTX *,
    int (*)(const SSL *, int *, void *));
"""

CUSTOMIZATIONS = """
#ifdef OPENSSL_NO_SSL2
static const int Cryptography_HAS_SSL2 = 0;
SSL_METHOD* (*SSLv2_method)() = NULL;
SSL_METHOD* (*SSLv2_client_method)() = NULL;
SSL_METHOD* (*SSLv2_server_method)() = NULL;
#else
static const int Cryptography_HAS_SSL2 = 1;
#endif

#ifdef SSL_CTRL_SET_TLSEXT_HOSTNAME
static const int Cryptography_HAS_TLSEXT_HOSTNAME = 1;
#else
static const int Cryptography_HAS_TLSEXT_HOSTNAME = 0;
void (*SSL_set_tlsext_host_name)(SSL *, char *) = NULL;
const char* (*SSL_get_servername)(const SSL *, const int) = NULL;
void (*SSL_CTX_set_tlsext_servername_callback)(
    SSL_CTX *,
    int (*)(const SSL *, int *, void *)) = NULL;
#endif
"""
