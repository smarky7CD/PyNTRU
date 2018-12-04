# PyNTRU

This is my version of NTRUEncrypt written in Python 3. It is currently for research purposes only. I strongly reccomend (perhaps demand) that this implementation is not used for sensitive data. It has not been vetted and is probably insecure.


## Install

```bash

git clone https://github.com/smarky7CD/PyNTRU.git

pip3 install -r requirements.txt

```

## Using

As this is purley for research, there is not much of a higher level API exposed. Although the ```ntru_key_object.py``` would be the place to go for those interested. Also, check out the ```keys``` directory.

## Change Log

[Change Log](https://github.com/smarky7CD/PyNTRU/blob/master/changelog.md)

## Testing

### Unit Tests

* Polynomial: Passing
* NTRU Polynomial Operations: Passing
* NTRU Parameters (Polynomial Generation): Passing
* Encryption and Decryption: Passing
* NTRUKey Object: Passing

### User Testing
* Key Exporting and Importing: Pssing

