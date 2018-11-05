pragma solidity ^0.4.7;
import "remix_tests.sol"; // this import is automatically injected by Remix.

contract Clear {
    address whom;
    string data;
    uint8 yays;
    uint8 nays;
    uint8 pending;
    mapping(address=>uint8) verifiers;
    
    function Clear(string data, address tempwhom, address[] verifier) public {
        whom = tempwhom;
        bool is_member = (msg.sender == tempwhom) ? true : false;
        for(uint8 v = 0; v < verifier.length; v++){
            if (verifier[v] == msg.sender){
                is_member = true;
            }
            pending++;
            verifiers[verifier[v]] = 2;
        }
    }
    
    function attest(bool verify) public{
        if (verifiers[msg.sender] == 2){
            verifiers[msg.sender] = verify ? 1 : 0;
            if(verifiers[msg.sender]==1)
                yays++;
            else
                nays++;
            pending--;
        }
    }
    
    function result() constant public returns(uint8){
        return yays >= nays ? 1 : 0;
    }
    
    function result_arr() constant public returns(uint8[3]){
        return [yays, nays, pending];
    }
    
    function add_verifier(address verifier) public{
        if(msg.sender != whom)
            return;
        verifiers[verifier] = 2;
    }
    
    function get_data() constant public returns(string){
        return data;
    }
}

