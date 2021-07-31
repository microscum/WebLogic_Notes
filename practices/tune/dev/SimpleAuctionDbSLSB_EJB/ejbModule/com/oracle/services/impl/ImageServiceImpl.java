
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.oracle.services.impl;

import com.oracle.model.Image;
import com.oracle.services.ImageService;

import java.util.logging.Level;
import java.util.logging.Logger;

import javax.annotation.Resource;
import javax.ejb.Local;
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.UserTransaction;

@Stateless(name = "ImageService")
@Local(ImageService.class)
public class ImageServiceImpl {

  private static final Logger LOG = Logger.getLogger(ImageServiceImpl.class.getName());
  @PersistenceContext(unitName = "AuctionPU")
  private EntityManager em;
  @Resource
  private UserTransaction utx;

  public ImageServiceImpl() {
  }

  public Image findImageById(int imageId) {
    Image image = null;
    try {
      image = em.find(Image.class, imageId);
    } catch (Exception e) {
      LOG.log(Level.SEVERE, e.getMessage());
    }
    return image;
  }

  public Image addImage(Image image) {
    try {
      //utx.begin();
      em.persist(image);
      //utx.commit();
      return image;
    } catch (Exception ex) {
      Logger.getLogger(ImageServiceImpl.class.getName()).log(Level.SEVERE, null, ex);
      throw new RuntimeException(ex);
    }
  }
}