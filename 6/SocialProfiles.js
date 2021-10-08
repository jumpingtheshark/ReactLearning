import React, {Component} from "react";
import SOCIAL_PROFILES from '../data/socialProfiles'
import emailIcon from "../assets/profile.png";

//<a href="https://www.qries.com/">
 //   <img alt="Qries" src="https://www.qries.com/images/banner_logo.png"
 //        width=150" height="70">
//</a>


class SocialProfile extends Component {

    // id: 1,
    // link: 'mailto:dkcodehelper@gmail.com',
    // image: emailIcon


    render()
    {
        const { id, link, image } = this.props.profile


        return (
            <span>
                <a href={link}>
                      <img alt="Qr" src={image}  style={{ width:20, height:20, margin:10}} />
                </a>


            </span>

        )

    }

}





class SocialProfiles extends Component {




    render(){

        return (
         <div>
        SocialProfiles Component
             <p>

                 {
                     SOCIAL_PROFILES.map(
                         (x)=>{
                             return (
                                 <SocialProfile
                                 key = {x.id}
                                 profile = {x}
                                 >
                                 </SocialProfile>
                             )

                         }

                     )
                 }

             </p>

        </div>
        )
    }


}

export default SocialProfiles;