
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.oracle;

import com.oracle.model.Auction;
import com.oracle.model.Bid;
import com.oracle.model.Image;
import com.oracle.sampleData.AuctionData;
import com.oracle.sampleData.AuctionDataSet;
import com.oracle.services.AuctionService;
import com.oracle.services.ImageService;


public class SetupDatabase {
  private AuctionService auctionService;
  private ImageService imageService;

  public static void main(String [] args) {
    SetupDatabase setup = new SetupDatabase();
    setup.imageService = new ImageService();
    setup.auctionService = new AuctionService();
    setup.createDatabase();
  }
  
  public void createDatabase() {
    AuctionDataSet dataSet = new AuctionDataSet();
    //for (AuctionData data : dataSet.getDataList()) {
    //	System.out.println("DEBUG: AuctionDataSet = " + data.getAuction().toString());
    //}
    for (AuctionData data : dataSet.getDataList()) {
      if (data.getImage() != null) {
        Image savedImage = imageService.addImage(data.getImage());
        data.setImage(savedImage);
      }
      Auction savedAuction = auctionService.addAuction(data.getAuction());
      data.setAuction(savedAuction);
      for (Bid bid : data.getBids()) {
        auctionService.bid(data.getAuction().getAuctionId(), bid.getBidder(), bid.getAmount());
      }
    }
    System.out.println("Database created.");
  }
}
