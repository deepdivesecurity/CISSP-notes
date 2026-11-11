# Certificates & Digital Signatures

## Certificates
- Contains individual's public key
- Signed by certificate authority using their private key
- Recipient uses CA's public key to verify

## Digital Signatures
1. Sender hashes message
2. Sender signs hash with their private key
3. Sender sends the message and digital signature
4. Recipient hashes message
5. Recipient uses sender's public key to verify digital signature
6. Recipient compares verified hash with the newly calculated hash