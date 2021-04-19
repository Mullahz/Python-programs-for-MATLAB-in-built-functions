def col2im(blk_mtx, img, blk_size):
  image_size = img.shape
  imgw = img.shape[0]
  imgh = img.shape[1]

  p, q = [blk_size, blk_size]

  result = np.zeros(image_size)
  weight = np.zeros(image_size)

  #blk_mtx     =  blk_mtx.astype(np.int64)
  #result      =  result.astype(np.float64)
  #weight      =  weight.astype(np.int64)

  col = 0
  for i in range(1,imgw,blk_size):
    for j in range(1,imgh,blk_size):
      result[j-1:j + p-1, i-1:i + q-1] += blk_mtx[:, col].reshape((blk_size, blk_size), order='F')
      weight[j-1:j + p-1, i-1:i + q-1] += np.ones((blk_size, blk_size))
      col += 1
  
  final_res = np.divide(result,weight)
  final_res_1=final_res.T

  return final_res_1
