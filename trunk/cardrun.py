#!/usr/bin/end python3

def safe_float(obj):
    'safe version of float()'
    try:
        reval = float(obj)
    except (ValueError,TypeError):
        reval = str(diag)
    return reval

def main():
    'handles all the data processing'
    log = open('cardlog.txt','w')
    try:
        ccfile = open('carddata.txt','r')
    except IOError:
        log.write('no txns this monyh\n')
        log.close()
        return

    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result,float):
            total += result
            log.write('data...processed\n')
    print('$%.2f (new balance)' % (total))
    log.close()

if __name__ == '__main__':
    main()