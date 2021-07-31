
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.oracle.services;

import com.oracle.model.Image;
import com.oracle.services.ImageService;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
//import javax.persistence.PersistenceContext;
//import javax.transaction.UserTransaction;

public class ImageService {
  private static EntityManagerFactory	emf;
  //@PersistenceContext(unitName = "AuctionPU")
  private EntityManager em;
  
  private EntityTransaction utx;

  public ImageService() {
	initEMF();
	em = emf.createEntityManager();
  }

  public Image findImageById(int imageId) {
    Image image = null;
    try {
      image = em.find(Image.class, imageId);
    } catch (Exception e) {
      System.out.println(e.getMessage());
    }
    return image;
  }

  public Image addImage(Image image) {
    try {
      utx = em.getTransaction();
      utx.begin();
      em.persist(image);
      utx.commit();
      return image;
    } catch (Exception ex) {
      System.out.println(ex);
      throw new RuntimeException(ex);
    }
  }
  
  private static synchronized void initEMF()
  {
	if (emf == null)
	{
		emf = Persistence.createEntityManagerFactory("AuctionPU");
	}
  }
}