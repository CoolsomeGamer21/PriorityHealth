<html>
import Deso from 'deso-protocol';
const deso = new Deso();
const request = 3;
 const response = await deso.identity.login(request);
 
 import Deso from 'deso-protocol';
const deso = new Deso();
const request = ;
 const response = await deso.identity.logout(request);

import Deso from 'deso-protocol';
const deso = new Deso();
const request = {
  "PublicKeyBase58Check": "BC1YLheA3NepQ8Zohcf5ApY6sYQee9aPJCPY6m3u6XxCL57Asix5peY"
};
 const response = await deso.user.getSingleProfile(request);
 
 import Deso from 'deso-protocol';
const deso = new Deso();
const request = BC1YLheA3NepQ8Zohcf5ApY6sYQee9aPJCPY6m3u6XxCL57Asix5peY;
 const response = await deso.user.getSingleProfilePicture(request);
</html>
