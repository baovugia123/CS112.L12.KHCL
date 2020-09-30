#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Abstraction: 
    - Tìm n sau khi duyệt hết mảng 1 chiều


# In[ ]:


2. Decomposition:
    - Sắp xếp mảng
    - So sánh n với từng phần tử của mảng
    - In ra kết quả cần tìm


# In[ ]:


3. Pattern Recognition:
    - Quy hoạch động


# In[ ]:


4. Algorithm designed:
    Input: n, các phần tử của mảng c[]
    Output: H_Index
  Mã giả:
    Nhập n
    If n>0
       Khởi tạo mảng c[]
       Nhập các phần tử mảng c[]
       Sắp xếp mảng
    Chạy vòng for i->n, i=0
       If c[i]<n
        n=n-1
       If c[i]>=n
        break
    Xuất n 


# In[ ]:


Code:
   n = int(input())
   if (n > 0):
           c = []
           c = list(map(int, input().split()))
           c.sort()
   for i in range(0,n):
       if(c[i] < n):
               n = n - 1
    if(c[i] >= n):
              break          
   print(n)

