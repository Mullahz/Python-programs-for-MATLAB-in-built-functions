def im2col(img,blk_size):
  imgw = img.shape[0]
  imgh = img.shape[1]
  
  mtx = img
  m2 = (blk_size,blk_size)
  blk = np.zeros(m2)
  
  m1c = 0
  for i in range(1,imgw,blk_size):
    for j in range(1,imgh,blk_size):
      m1c = m1c+1
  m1 = ((blk_size*blk_size),m1c)
  blk_mtx = np.zeros(m1)
  
  itr = 0
  for i in range(1,imgw,blk_size):
    for j in range(1,imgh,blk_size):
      blk = mtx[i-1:i+blk_size-1, j-1:j+blk_size-1]
      blk1 = blk.flatten()
      itr = itr+1
      blk_mtx[:,itr-1] = blk1  
  return blk_mtx
