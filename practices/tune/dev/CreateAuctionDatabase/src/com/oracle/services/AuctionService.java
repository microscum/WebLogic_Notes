
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.oracle.services;

import com.oracle.model.Auction;
import com.oracle.model.Bid;
import com.oracle.services.AuctionService;
import com.oracle.util.AuctionUtil;

import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

import javax.annotation.Resource;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
//import javax.persistence.PersistenceContext;
import javax.persistence.Query;
//import javax.transaction.UserTransaction;

@SuppressWarnings("unused")
public class AuctionService {
  
  private final Map<Integer, Auction> auctions;
  private final Map<Integer, Bid> bids;
  private int currentAuctionId = 100;
  private int currentBidId = 10;
  
  private static EntityManagerFactory	emf;
  //@PersistenceContext(unitName = "AuctionPU")
  private EntityManager em;
  private EntityTransaction utx;

  public AuctionService() {
	initEMF();
	em = emf.createEntityManager();
	auctions = new HashMap<Integer, Auction>();
    bids = new HashMap<Integer, Bid>();
  }

  @SuppressWarnings("unchecked")
  public List<Auction> getAllAuctions() {
    Query query = em.createQuery("Select a FROM Auction a");
    return query.getResultList();
  }

  public Auction addAuction(Auction auction) {
    try {
      utx = em.getTransaction();
      utx.begin();
      em.persist(auction);
      utx.commit();
      return auction;
    } catch (Exception e) {
      System.out.println(e.getMessage());
      throw new RuntimeException(e);
    }
  }

  public Auction findAuctionById(int auctionId) {
	Auction auction = null;
    try {
      auction = em.find(Auction.class, auctionId);
    } catch (Exception e) {
    	System.out.println(e.getMessage());
    }
    return auction;
  }

  public Auction updateAuction(Auction auction) {
    try {
      utx = em.getTransaction();
      utx.begin();
      int auctionId = auction.getAuctionId();
      em.find(Auction.class, auctionId);
      auction = em.merge(auction);
      utx.commit();
      return auction;
    } catch (Exception ex) {
    	System.out.println(ex);
      throw new RuntimeException(ex);
    }
  }

  public String bid(int auctionId, String bidder, float bidAmount) {
    int id = currentBidId;
    currentBidId++;
    Auction auction = findAuctionById(auctionId);
    if (bidder.equals(auction.getHighestBidder())) {
      //same bidder, errror.
      return "Bid failed, You cannot bid when you are the highest bidder.";
    }
    if (bidAmount < auction.getCurrPrice() + auction.getIncrement()) {
      // not enough $ - error
      return "Bid failed, You cannot bid less than the next bid.";
    }
    auction.setHighestBidder(bidder);
    auction.setCurrPrice(bidAmount);
    auction.setIncrement(AuctionUtil.defineIncrement(bidAmount));
    Bid bid = new Bid(id, bidder, auction, bidAmount, new Date());
    auction.addBid(bid);
    bids.put(id, bid);
    updateAuction(auction);
    return "Bid Successful";
  }
  
  private static synchronized void initEMF()
  {
	if (emf == null)
	{
		emf = Persistence.createEntityManagerFactory("AuctionPU");
	}
  }
}