import React, {Component} from 'react'

const TITLES = [
    'a software engineer',
    ' a music lover',
    'an enthusiastic learner',
    'an adventure seeker'

];

class Title extends Component {
    state={ti: 0, fadeIn: true};

    componentDidMount() {
        console.log('Title component has loaded')
        this.animateTitles()

    }

    // I think that we are doing this weird arrow notation so that we don't have to have a constructor
    // and do all that this.register stuff
    // it goes somethign like
    // this.f=f.register() or something like that.  Looks nonsensical, but I need to look more into this.
    animateTitles= ()=> {
        //alert (this.state.ti)
        this.titleInterval=setInterval(
            ()=>{
                        //alert(this.state.ti)
                        const _titleIndex= ((this.state.ti +1) % TITLES.length);
                        this.setState({ti: _titleIndex});
            }
        , 4000);
        console.log ('this.titleInterval', this.titleInterval);

    }

componentWillUnmount() {
    console.log('Title component will unmount')
    clearInterval (this.titleInterval)

}


    render (){
        const {fadeIn, titleIndex}=this.state;
        const title= TITLES[this.state.ti]
        return (
            <p className={fadeIn ? 'title-fade-in':'title-fade-out'}>
                I am {title}
            </p>

        )
    }



}


export default Title;