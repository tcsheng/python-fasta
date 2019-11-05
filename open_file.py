#!/usr/bin/env python
# coding: utf-8

# In[1]:


def read_fasta(filename):
    """
    Read a FASTA file sequence from the named file
    """
    seq=''
    f=open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            seq=seq+line
    f.close()
    return seq
read_fasta('ae.fa')


# In[ ]:




