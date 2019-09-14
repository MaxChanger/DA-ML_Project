#########################################
# 2019-08-31 Jiadai Sun
# sunjiadai@foxmail.com
# 
# python .\readMail.py
# 
#########################################

import imaplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import time

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos+8:].strip()
    return charset

def guess_filename(msg):

    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('name=')
        if pos >= 0:
            charset = content_type[pos+5:].strip()
    return charset

def print_info(msg, indent=0, writefile = True):
    # print(msg)
    if indent == 0:
        for header in ['From', 'To', 'Subject', 'Date']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                elif header == 'Date':
                    value = value
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' ' * indent, header, value))

    if (msg.is_multipart()):
        parts = msg.get_payload()   # 返回list，包含所有的子对象:
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s--------------------' % (' ' * indent))
            print_info(part, indent + 1)    # 递归打印每一个子对象:
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)    # 检测文本编码
            if charset:
              content = content.decode(charset)
            print('%sText: %s' % (' ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % (' ' * indent, content_type))    # 不是文本,作为附件处理:


def printHEAD(msg, order):
    print('\n//--------------------The {0}th unseen e-mail--------------------//'.format('%03d'%(order+1)))
    for header in ['From', 'To', 'Subject', 'Date']:
        value = msg.get(header, '')
        if value:
            if header == 'Subject':
                value = decode_str(value)
            elif header == 'Date':
                value = value
            else:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = u'%s <%s>' % (name, addr)
        print('%s: %s' % ( header, value))


def printOther(msg, indent = 0):
    if (msg.is_multipart()):
        parts = msg.get_payload()   # 返回list，包含所有的子对象:
        for n, part in enumerate(parts):
            # print('%spart %s' % (' ' * indent, n))
            # print('%s--------------------' % (' ' * indent))
            printOther(part, indent + 1)    # 递归打印每一个子对象:
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain': #or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)    # 检测文本编码
            if charset:
                content = content.decode(charset)
            print('--Text:\n %s' % (content))
        elif content_type=='application/octet-stream':
            filename = guess_filename(msg)
            print('--Attachment:',filename)


def printINFO(msg, order):
    printHEAD(msg, order)
    printOther(msg)

if __name__=='__main__':

    try:
        imap = imaplib.IMAP4_SSL('imap.qq.com','993')
        imap.login('user_name','password')
        print("Login successfully")
    except Exception as e:
        print('Login failed' + str(e))

    result, message = imap.select('INBOX')      
    type, data = imap.search(None, 'UNSEEN')    #'ALL')
    newlist=data[0].split()

    while True:
        for i in range(0, len(newlist)):
            type, data = imap.fetch(newlist[i], '(RFC822)') # type=ok
            msg = email.message_from_string(data[0][1].decode('utf-8'))
            printINFO(msg, i)

        time.sleep(5)