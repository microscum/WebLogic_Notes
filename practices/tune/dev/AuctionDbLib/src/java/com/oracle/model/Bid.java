
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.oracle.model;

import java.io.Serializable;
import java.util.Date;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.SequenceGenerator;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

@Entity
public class Bid implements Serializable {

  private static final long serialVersionUID = 1L;
  
  @SequenceGenerator(name="bid_sequence", sequenceName="bidid_sequence", allocationSize=1)
  @GeneratedValue(strategy=GenerationType.SEQUENCE, generator="bid_sequence")
  @Id
  private int bidId;
  private String bidder;
  @ManyToOne
  @JoinColumn(name = "AUCTIONID")
  private Auction auction;
  private float amount;
  @Temporal(TemporalType.TIMESTAMP)
  private Date bidTime;

  public Bid() {
  }

  public Bid(int bidId, String bidderId, Auction auction, float amount, Date bidTime) {
    this.bidId = bidId;
    this.bidder = bidderId;
    this.auction = auction;
    this.amount = amount;
    this.bidTime = bidTime;
  }

  public int getBidId() {
    return bidId;
  }

  public void setBidId(int bidId) {
    this.bidId = bidId;
  }

  public String getBidder() {
    return bidder;
  }

  public void setBidder(String bidderId) {
    this.bidder = bidderId;
  }

  public Auction getAuction() {
    return auction;
  }

  public void setAuction(Auction auction) {
    this.auction = auction;
  }

  public float getAmount() {
    return amount;
  }

  public void setAmount(float amount) {
    this.amount = amount;
  }

  public Date getBidTime() {
    return bidTime;
  }

  public void setBidTime(Date bidTime) {
    this.bidTime = bidTime;
  }
}